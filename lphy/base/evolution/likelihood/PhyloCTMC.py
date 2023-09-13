from abc import ABC

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class PhyloCTMC(GenerativeDistribution, ABC):

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, tree: Value, Q: Value, L=None, mu=None, siteRates=None,
                 branchRates=None, dataType=None, root=None):
        super().__init__()
        # have to take Value.value
        self.tree = tree
        self.Q = Q
        self.L = L
        self.mu = mu  # branchRates in dnPhyloCTMC
        self.siteRates = siteRates
        self.branchRates = branchRates
        self.dataType = dataType
        self.root = root  # dnPhyloCTMC not support

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)


    # TODO
    # dnPhyCTMC siteRates are the rates of each category not each site, which has the same length of ncat
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        tree_name = "tree"
        tree = self.get_param(tree_name)
        q_name = "Q"
        q = self.get_param(q_name)

        builder = [get_argument_rev_string(tree_name, tree), get_argument_rev_string(q_name, q)]
        #TODO optional
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

#TODO: data clamp here or in builder?
# seq ~ dnPhyloCTMC(tree=psi, Q=Q, siteRates=sr, pInv=p_inv, type="DNA", branchRates=clock)
# seq.clamp(sequences)

