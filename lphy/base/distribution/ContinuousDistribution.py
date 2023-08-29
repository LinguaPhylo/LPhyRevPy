from collections import OrderedDict

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class LogNormal(GenerativeDistribution):

    def __init__(self, meanlog: Value, sdlog: Value, offset=None):
        super().__init__()
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset if offset is not None else Value(None, 0.0)

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

