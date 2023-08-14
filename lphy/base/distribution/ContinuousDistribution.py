from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable


class LogNormal(GenerativeDistribution):

    def __init__(self, meanlog, sdlog, offset=0):
        super().__init__()
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(None, id_, self)
