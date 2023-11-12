from lphy.base.evolution.tree.TaxaConditionedTreeGenerator import TaxaConditionedTreeGenerator
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class FullBirthDeathTree(TaxaConditionedTreeGenerator):
    """
    David G. Kendall. On the Generalized "Birth-and-Death" Process,
    The Annals of Mathematical Statistics, Ann. Math. Statist. 19(1), 1-15, March, 1948.
    https://doi.org/10.1214/aoms/1177730285
    """
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "FullBirthDeath",
                      "description": "A birth-death tree with both extant and extinct species. "
                                     "Conditioned on age of root or origin."}

    def __init__(self, lambda_: Value, mu: Value, rootAge: Value = None, originAge: Value = None):
        # this is more restrict, to avoid requiring extra Rev code to create taxa
        # if (rootAge is not None and originAge is not None) or (rootAge is None and originAge is None):
        #     raise ValueError("Only one of rootAge and originAge may be specified, but not both or neither !")

        super().__init__()
        self.lambda_ = lambda_  # per-lineage birth rate.
        self.mu = mu  # per-lineage death rate.
        self.rootAge = rootAge  # the age of the root.
        self.originAge = originAge  # the age of the origin.

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    # https://revbayes.github.io/documentation/dnBirthDeath.html
    def lphy_to_rev(self, var_name):
        # TODO
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException()

        # TODO Rev requires taxa ?
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("in dev !")

        # lphy names are same to rev
        mu_name = "mu"
        lambda_ = self.get_param("lambda_")
        mu = self.get_param(mu_name)

        #TODO check if condition="survival" is correct

        builder = [get_argument_rev_string("lambda", lambda_), get_argument_rev_string(mu_name, mu),
                   'condition="survival"']

        root_age_name = "rootAge"
        if self.rootAge is not None:
            root_age = self.get_param(root_age_name)
        elif self.originAge is not None:
            root_age = self.get_param("originAge")
        else:
            raise ValueError("Only one of rootAge and originAge may be specified, but not both or neither !")
        builder.append(get_argument_rev_string(root_age_name, root_age))

        args = ", ".join(builder)
        return f"dnBDP({args})"


