from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class Coalescent(GenerativeDistribution):

    def __init__(self, theta: Value, n: Value = None, taxa: Value = None):
        if (n is not None and taxa is not None) or (n is None and taxa is None):
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")

        super().__init__()
        self.theta = theta
        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        theta_name = "theta"
        taxa_name = "taxa"
        theta = self.get_param(theta_name)
        if self.taxa is not None:
            taxa = self.get_param(taxa_name)
            #TODO https://revbayes.github.io/documentation/dnHeterochronousCoalescent.html
            return f"dnCoalescent({get_argument_rev_string(theta_name, theta)}, {get_argument_rev_string(taxa_name, taxa)})"
        elif self.n is not None:
            n = self.n.value
            from lphy.core.error.Errors import UnsupportedOperationException
            raise UnsupportedOperationException("TODO !")
        else:
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")
