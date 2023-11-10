from abc import ABC
from collections import OrderedDict

import numpy as np
from scipy.linalg import expm

from lphy.base.evolution.alignment.Alignment import Alignment
from lphy.base.evolution.tree.TimeTree import TimeTree
from lphy.base.evolution.tree.TimeTreeNode import TimeTreeNode
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class PhyloCTMC(GenerativeDistribution, ABC):

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, tree: Value, Q: Value, L=None, mu=None, freq=None, siteRates=None,
                 branchRates=None, dataType=None, root=None):
        super().__init__()
        # have to take Value.value
        self.tree = tree
        self.Q = Q
        self.L = L
        self.mu = mu  # branchRates in dnPhyloCTMC
        self.root_freqs = freq  # root frequencies
        self.siteRates = siteRates
        self.branch_rates = branchRates
        self.dataType = dataType
        self.root = root  # root sequence, dnPhyloCTMC not support

        self.id_map = OrderedDict()
        self.trans_prob = None  # Initialize as needed
        self.decomposition = None  # Initialize as needed
        self.ievc = None  # Initialize as needed
        self.evec = None  # Initialize as needed
        self.iexp = None  # Initialize as needed
        self.eval = None  # Initialize as needed

    def sample(self, id_: str = None) -> "RandomVariable":
        # setup
        self.compute_p_and_root_freqs()

        # TODO

        # Default to nucleotide
        dt = SequenceType.NUCLEOTIDE if self.data_type is None else self.data_type

        length = self.get_site_count()

        a = Alignment(self.id_map, length, dt)

        mu = 1.0 if self.clock_rate is None else float(self.clock_rate)

        for i in range(length):
            if self.root_seq is not None:
                # Use simulated or user-specified root sequence
                root_state = self.root_seq.get_state(0, i)  # Root taxon is 0
                self.traverse_tree(self.tree.get_root(), root_state, a, i, self.trans_prob, mu,
                                   1.0 if self.site_rates is None else self.site_rates[i])
            else:
                from lphy.base.distribution.DiscreteDistribution import Categorical
                root_state = Categorical.sample(self.root_freqs)
                self.traverse_tree(self.tree.get_root(), root_state, a, i, self.trans_prob, mu,
                                   1.0 if self.site_rates is None else self.site_rates[i])

        return RandomVariable(id_, a, self)

    # dnPhyCTMC siteRates are the rates of each category not each site, which has the same length of ncat
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        tree_name = "tree"
        tree = self.get_param(tree_name)
        q_name = "Q"
        q = self.get_param(q_name)

        builder = [get_argument_rev_string(tree_name, tree), get_argument_rev_string(q_name, q)]
        # TODO optional
        # lphy name diff to rev
        if self.L is not None:
            l = self.get_param("L")
            builder.append(get_argument_rev_string("nSites", l))
        if self.mu is not None:
            mu = self.get_param("mu")
            # rev branchRates is just 1 number, equivalent to lphy mu
            builder.append(get_argument_rev_string("branchRates", mu))
        if self.siteRates is not None:
            site_rates = self.get_param("siteRates")
            builder.append(get_argument_rev_string("siteRates", site_rates))
        if self.dataType is not None:
            data_type = self.get_param("dataType")
            builder.append(get_argument_rev_string("type", data_type))
        if self.root is not None:
            raise UnsupportedOperationException("dnPhyloCTMC does not support root sequence !\n"
                                                "https://revbayes.github.io/documentation/dnPhyloCTMC.html")

        args = ", ".join(builder)
        return f"dnPhyloCTMC({args})"

    # TODO: data clamp here or in builder?
    # seq ~ dnPhyloCTMC(tree=psi, Q=Q, siteRates=sr, pInv=p_inv, type="DNA", branchRates=clock)
    # seq.clamp(sequences)

    def get_Q(self):
        return self.Q.value

    def compute_p_and_root_freqs(self):
        self.id_map.clear()
        tree: TimeTree = self.tree.value
        self.fill_id_map(tree.get_root(), self.id_map)

        Qm = self.get_Q()
        if Qm is None:
            raise ValueError("Matrix Q[][] must be provided!")

        num_states = len(Qm)
        self.trans_prob = np.zeros((num_states, num_states))
        self.iexp = np.zeros((num_states, num_states))

        primitive = np.copy(Qm)
        Qmatrix = expm(primitive)

        eigenvalues, eigenvectors = np.linalg.eig(Qmatrix)
        self.Eval = eigenvalues
        self.Evec = eigenvectors

        self.Ievc = np.zeros((num_states, num_states))
        self.lu_inverse(self.Evec, self.Ievc, num_states)

        if self.root_freqs is None:
            self.root_freqs = self.compute_equilibrium(self.trans_prob)

    def traverse_tree(self, node: TimeTreeNode, node_state, alignment: Alignment, pos, trans_prob, clock_rate,
                      site_rate):
        if node.is_leaf() or (node.is_single_child_non_origin() and node.get_id() is not None):
            alignment.set_state(node.leaf_index, pos, node_state)
        children = node.children
        for child in children:
            branch_length = site_rate * clock_rate * (node.age - child.age)

            if self.branch_rates is not None:
                branch_length *= self.branch_rates[child.index]

            self.get_transition_probabilities(branch_length, trans_prob)
            state = self.draw_state(trans_prob[node_state])

            self.traverse_tree(child, state, alignment, pos, trans_prob, clock_rate, site_rate)

    ### private ?

    def compute_equilibrium(self, trans_prob):
        self.get_transition_probabilities(100, trans_prob)
        freqs = [trans_prob[0][i] for i in range(len(trans_prob))]
        for i in range(len(freqs)):
            for j in range(1, len(freqs)):
                if abs(trans_prob[0][i] - trans_prob[j][i]) > 1e-5:
                    print("WARNING: Branch length used to get equilibrium distribution was not long enough!")
        return freqs

    def fill_id_map(self, node: TimeTreeNode, id_map):
        if node.is_leaf() or node.get_id() is not None:
            i = id_map.get(node.get_id())
            if i is None:
                next_value = 0
                for j in id_map.values():
                    if j >= next_value:
                        next_value = j + 1
                id_map[node.get_id()] = next_value
                node.leaf_index = next_value
            else:
                node.leaf_index = i
        for child in node.children:
            self.fill_id_map(child, id_map)

    def draw_state(self, p):
        U = np.random.random()
        total_p = p[0]
        if U <= total_p:
            return 0
        for i in range(1, len(p)):
            total_p += p[i]
            if U <= total_p:
                return i
        if abs(total_p - 1.0) < 1e-6:
            return len(p) - 1
        raise RuntimeError(f"p vector should add to 1.0 but adds to {total_p} instead.")

    def get_transition_probabilities(self, branch_length, trans_probs):
        num_states = len(trans_probs)

        for i in range(num_states):
            temp = np.exp(branch_length * self.Eval[i])
            for j in range(num_states):
                self.iexp[i][j] = self.Ievc[i][j] * temp

        for i in range(num_states):
            for j in range(num_states):
                temp = 0.0
                for k in range(num_states):
                    temp += self.Evec[i][k] * self.iexp[k][j]
                trans_probs[i][j] = abs(temp)

    # TODO should this return imtrx instead ?
    def lu_inverse(self, inmat, imtrx, size):
        EPSILON = 2.220446049250313E-16
        i, j, k, l, maxi, idx, ix, jx = 0, 0, 0, 0, 0, 0, 0, 0
        sum, tmp, maxb = 0.0, 0.0, 0.0
        index = np.zeros(size)

        omtrx = np.zeros((size, size))
        # copy inmat to omtrx
        for i in range(size):
            for j in range(size):
                omtrx[i][j] = inmat[i][j]

        aw = 1.0
        wk = np.zeros(size)
        for i in range(size):
            maxb = 0.0
            for j in range(size):
                if abs(omtrx[i][j]) > maxb:
                    maxb = abs(omtrx[i][j])
            if maxb == 0.0:
                raise ValueError("Singular matrix encountered")
            wk[i] = 1.0 / maxb

        for j in range(size):
            for i in range(j):
                sum = omtrx[i][j]
                for k in range(i):
                    sum -= omtrx[i][k] * omtrx[k][j]
                omtrx[i][j] = sum

            maxb = 0.0
            for i in range(j, size):
                sum = omtrx[i][j]
                for k in range(j):
                    sum -= omtrx[i][k] * omtrx[k][j]
                omtrx[i][j] = sum
                tmp = wk[i] * abs(sum)
                if tmp >= maxb:
                    maxb = tmp
                    maxi = i

            if j != maxi:
                for k in range(size):
                    tmp = omtrx[maxi][k]
                    omtrx[maxi][k] = omtrx[j][k]
                    omtrx[j][k] = tmp
                aw = -aw
                wk[maxi] = wk[j]

            index[j] = maxi

            if omtrx[j][j] == 0.0:
                omtrx[j][j] = EPSILON

            if j != size - 1:
                tmp = 1.0 / omtrx[j][j]
                for i in range(j + 1, size):
                    omtrx[i][j] *= tmp

        for jx in range(size):
            for ix in range(size):
                wk[ix] = 0.0

            wk[jx] = 1.0
            l = -1

            for i in range(size):
                idx = index[i]
                sum = wk[idx]
                wk[idx] = wk[i]
                if l != -1:
                    for j in range(l, i):
                        sum -= omtrx[i][j] * wk[j]
                elif sum != 0.0:
                    l = i
                wk[i] = sum

            for i in range(size - 1, -1, -1):
                sum = wk[i]
                for j in range(i + 1, size):
                    sum -= omtrx[i][j] * wk[j]
                wk[i] = sum / omtrx[i][i]

            for ix in range(size):
                imtrx[ix][jx] = wk[ix]

        wk = None
        index = None
        omtrx = None
