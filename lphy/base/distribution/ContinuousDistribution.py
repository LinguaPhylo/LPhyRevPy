from collections import OrderedDict

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class LogNormal(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, meanlog: Value, sdlog: Value, offset=None):
        super().__init__()
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset if offset is not None else Value(None, 0.0)

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        #TODO no offset ?
        mean = self.meanlog.value
        sd = self.sdlog.value
        return f"dnLognormal(mean={mean}, sd={sd})"


class Dirichlet(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, conc: Value):
        super().__init__()
        self.conc = conc
        if not isinstance(conc.value, list):
            raise RuntimeError(f"Expect list of concentration parameters for a Dirichlet distribution ! {conc.value}")
        if not all(isinstance(element, (int, float)) for element in conc.value):
            raise RuntimeError(f"The concentration parameters for a Dirichlet distribution must be numbers ! {conc.value}")

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        conc = self.conc.value
        return f"dnDirichlet(alpha={conc})"
