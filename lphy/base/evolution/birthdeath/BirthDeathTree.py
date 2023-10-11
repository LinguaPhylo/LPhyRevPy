from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class BirthDeathTree(GenerativeDistribution):
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

        super().__init__()
        self.lambda_ = lambda_  # per-lineage birth rate.
        self.mu = mu  # per-lineage death rate.
        self.rootAge = rootAge  # the age of the root.

        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

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

        args = ", ".join(builder)
        return f"dnBDP({args})"

    def rev_code_before(self, var_name):
        if self.n is not None:
            n = self.n.value
            from lphy.base.evolution.taxa.Taxa import create_n_taxa
            return create_n_taxa(n, var_name)
        else:
            pass
