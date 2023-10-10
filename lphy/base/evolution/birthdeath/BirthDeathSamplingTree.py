from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class BirthDeathSamplingTree(GenerativeDistribution):
    """
    Tanja Stadler, Roger Kouyos, ..., Sebastian Bonhoeffer,
    Estimating the Basic Reproductive Number from Viral Sequence Data,
    Molecular Biology and Evolution, Volume 29, Issue 1, January 2012.
    https://doi.org/10.1093/molbev/msr217
    """
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "BirthDeathSampling",
                      "description": "The Birth-death-sampling tree distribution over tip-labelled time trees. "
                                     "Conditioned on root age."}

    def __init__(self, lambda_: Value, mu: Value, rho: Value, rootAge: Value):
        super().__init__()
        self.lambda_ = lambda_  # per-lineage birth rate.
        self.mu = mu  # per-lineage death rate.
        self.rho = rho  # sampling proportion
        self.rootAge = rootAge  # the age of the root.

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    # https://revbayes.github.io/documentation/dnBirthDeath.html
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        lambda_ = self.get_param("lambda_")
        mu = self.get_param("mu")
        rho_name = "rho"
        rho = self.get_param(rho_name)
        root_age_name = "rootAge"
        root_age = self.get_param(root_age_name)

        builder = [get_argument_rev_string("lambdaRates", lambda_), get_argument_rev_string("muRates", mu),
                   get_argument_rev_string(rho_name, rho), get_argument_rev_string(root_age_name, root_age)]

        args = ", ".join(builder)
        return f"dnEpisodicBirthDeath({args})"

