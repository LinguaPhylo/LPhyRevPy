from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class DiscretizeGamma(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, ncat: Value):
        super().__init__()
        self.shape = shape
        self.ncat = ncat

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        shape = self.shape.value
        ncat = self.shape.value
        return f"fnDiscretizeGamma(shape={shape}, rate={shape}, numCats={ncat})"



class Poisson(GenerativeDistribution):
    pass

