from lphy.base.evolution.tree.TaxaConditionedTreeGenerator import TaxaConditionedTreeGenerator
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class Yule(TaxaConditionedTreeGenerator):
    """
    death rate = 0
    """
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "Yule",
                      "description": "The Yule tree distribution over tip-labelled time trees. "
                                     "Will be conditional on the root age if one is provided."}

    def __init__(self, lambda_: Value, rootAge: Value = None, n: Value = None, taxa: Value = None):
        # this is more restrict, to avoid requiring extra Rev code to create taxa
        if (n is not None and taxa is not None) or (n is None and taxa is None):
            raise ValueError("Either 'n' or 'taxa' should be provided to 'BirthDeathTree', but not both or neither !")

        super().__init__()
        self.lambda_ = lambda_  # per-lineage birth rate.
        self.rootAge = rootAge  # the age of the root.

        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> RandomVariable:
        # TODO
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException()

        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    # https://revbayes.github.io/documentation/dnBirthDeath.html
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        taxa_name = "taxa"
        lambda_ = self.get_param("lambda_")

        # Rev mu Default : 0
        builder = [get_argument_rev_string("lambda", lambda_), "mu=0.0"]

        if self.rootAge is not None:
            root_age_name = "rootAge"
            root_age = self.get_param(root_age_name)
            builder.append(get_argument_rev_string(root_age_name, root_age))

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
