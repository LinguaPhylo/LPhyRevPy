from collections import OrderedDict

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class LogNormal(GenerativeDistribution):

    def __init__(self, meanlog: Value, sdlog: Value, offset=0):
        super().__init__()
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    def get_params(self):
        return OrderedDict([
            ("meanlog", self.meanlog),
            ("sdlog", self.sdlog)
        ])
        #TODO how about offset?
