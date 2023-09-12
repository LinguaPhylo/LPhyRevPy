from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.parser.RevBuilder import get_argument_rev_string


# This is also for Site Model.
class DiscretizeGamma(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, ncat: Value):
        super().__init__()
        self.shape = shape
        self.ncat = ncat

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    # Note: fnDiscretizeGamma is diff to DiscretizeGamma, the former returns the category rates, length == ncat,
    # but the latter returns the rate for one site, use IID to return site rates.
    def lphy_to_rev(self, var_name):
        shape_name = "shape"
        rate_name = "rate"
        ncat_name = "numCats"
        shape = self.get_param(shape_name)
        ncat = self.get_param("ncat")
        return (f"fnDiscretizeGamma({get_argument_rev_string(shape_name, shape)}, "
                f"{get_argument_rev_string(rate_name, shape)}, "
                f"{get_argument_rev_string(ncat_name, ncat)})")
#TODO ignore replicates=L in DiscretizeGamma, or better solution?


class Poisson(GenerativeDistribution):
    pass

