import math
import random
from lphy.base.evolution.tree.TaxaConditionedTreeGenerator import draw_random_node, TaxaConditionedTreeGenerator
from lphy.base.evolution.tree.TimeTreeNode import TimeTreeNode
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


def birth_death_internal_q(p, lambda_val, mu_val, root_height):
    if lambda_val == mu_val:
        return p * root_height / (1 + lambda_val * root_height * (1 - p))
    h = lambda_val - mu_val
    e1 = math.exp(-h * root_height)
    a1 = lambda_val - mu_val * e1
    a2 = p * (1 - e1)
    return (1 / h) * math.log((a1 - mu_val * a2) / (a1 - lambda_val * a2))


class BirthDeathTree(TaxaConditionedTreeGenerator):
    """
    Joseph Heled, Alexei J. Drummond, Calibrated Birth–Death Phylogenetic Time-Tree Priors for Bayesian Inference,
    Systematic Biology, Volume 64, Issue 3, May 2015. https://doi.org/10.1093/sysbio/syu089
    """
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "BirthDeath",
                      "description": "A tree of only extant species, which is conceptually embedded"
                                     "in a full species tree produced by a speciation-extinction (birth-death) "
                                     "branching process. Conditioned on root age and on number of taxa."}

    def __init__(self, lambda_: Value, mu: Value, rootAge: Value, n: Value = None, taxa: Value = None):
        # this is more restrict, to avoid requiring extra Rev code to create taxa
        if (n is not None and taxa is not None) or (n is None and taxa is None):
            raise ValueError("Either 'n' or 'taxa' should be provided to 'BirthDeathTree', but not both or neither !")

        super().__init__(n, taxa, None)
        self.lambda_ = lambda_  # per-lineage birth rate.
        self.mu = mu  # per-lineage death rate.
        self.rootAge = rootAge  # the age of the root.

        self.check_taxa_parameters(True)

    def sample(self, id_: str = None) -> RandomVariable:
        from lphy.base.evolution.tree.TimeTree import TimeTree

        tree = TimeTree(self.get_taxa())
        active_nodes = self.create_leaf_taxa(tree)

        lambda_val = float(self.lambda_.value)
        mu_val = float(self.mu.value)
        root_age_val = float(self.rootAge.value)

        times = [birth_death_internal_q(random.random(), lambda_val, mu_val, root_age_val) for _ in
                 range(len(active_nodes) - 1)]
        times[-1] = root_age_val
        times.sort()

        for i in range(len(times)):
            a = draw_random_node(active_nodes)
            b = draw_random_node(active_nodes)
            parent = TimeTreeNode(times[i], [a, b])
            active_nodes.append(parent)

        tree.set_root(active_nodes[0])

        return RandomVariable(id_, tree, self)

    # https://revbayes.github.io/documentation/dnBirthDeath.html
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        mu_name = "mu"
        taxa_name = "taxa"
        root_age_name = "rootAge"
        lambda_ = self.get_param("lambda_")
        mu = self.get_param(mu_name)
        root_age = self.get_param(root_age_name)

        builder = [get_argument_rev_string("lambda", lambda_), get_argument_rev_string(mu_name, mu),
                   get_argument_rev_string(root_age_name, root_age)]

        if self.taxa is not None:
            taxa = self.get_param(taxa_name)
            builder.append(get_argument_rev_string(taxa_name, taxa))
        elif self.n is not None:
            # here must be same as def rev_code_before(self, var_name):
            taxa_var_name = var_name + "_taxa"
            builder.append(f"taxa={taxa_var_name}")
        else:
            raise ValueError("Either 'n' or 'taxa' should be provided to 'BirthDeathTree', but not both or neither !")

        # TODO Rev dnBDP : The condition of the process. Default : time
        # hard code to set condition
        builder.append('samplingStrategy="uniform", condition="survival"')

        args = ", ".join(builder)
        return f"dnBDP({args})"

    def rev_code_before(self, var_name):
        if self.n is not None:
            n = self.n.value
            from lphy.base.evolution.taxa.Taxa import create_n_taxa
            return create_n_taxa(n, var_name)
        else:
            pass
