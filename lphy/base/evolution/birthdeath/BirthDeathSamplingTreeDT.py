from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.parser.UnicodeConverter import get_canonical


class BirthDeathSamplingTreeDT(GenerativeDistribution):
    """
    Tanja Stadler, Mammalian phylogeny reveals recent diversification rate shifts,
    Proceedings of the National Academy of Sciences, 108 (15), 2011.
    https://doi.org/10.1073/pnas.1016876108
    """
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "BirthDeathSampling",
                      "description": "The Birth-death-sampling tree distribution over tip-labelled time trees. "
                                     "Conditioned on root age."}

    # LPhy overloading, see BirthDeathSamplingTree
    def __init__(self, diversification: Value, turnover: Value, rho: Value, rootAge: Value):
        super().__init__()
        self.diversification = diversification  # diversification rate.
        self.turnover = turnover  # turnover.
        self.rho = rho  # sampling proportion
        self.rootAge = rootAge  # the age of the root.

    def sample(self, id_: str = None) -> RandomVariable:
        # turnoverst return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    # https://revbayes.github.io/documentation/dnBirthDeath.html
    def lphy_to_rev(self, var_name):
        # TODO Rev requires taxa ?
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("in dev !")

        # lphy names are same to rev
        turnover = self.get_param("turnover")
        rho_name = "rho"
        rho = self.get_param(rho_name)
        root_age_name = "rootAge"
        root_age = self.get_param(root_age_name)

        lambda_var_name = var_name + "_lambda"
        mu_var_name = var_name + "_mu"

        builder = [f"lambdaRates={lambda_var_name}", f"muRates={mu_var_name}",
                   get_argument_rev_string(rho_name, rho), get_argument_rev_string(root_age_name, root_age)]

        args = ", ".join(builder)
        return f"dnEpisodicBirthDeath({args})"


    def rev_code_before(self, var_name):
        lambda_var_name = var_name + "_lambda"
        mu_var_name = var_name + "_mu"

        diversification = self.get_param("diversification")
        turnover = self.get_param("turnover")

        # denom = abs(1.0 - turnover);
        # λ = diversification / denom;
        # death_rate = (turnover * diversification) / denom;

        divers_var_name = get_canonical(diversification.get_id())
        turnover_var_name = get_canonical(turnover.get_id())

        builder = [f"{var_name}_denom := abs(1.0 - {turnover_var_name})",
                   f"{lambda_var_name} := {divers_var_name} / {var_name}_denom",
                   f"{mu_var_name} := ({turnover_var_name} * {divers_var_name}) / {var_name}_denom"]

        return "\n".join(builder)

