from collections import OrderedDict

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class Coalescent(GenerativeDistribution):

    def __init__(self, theta: Value, n: Value = None, taxa: Value = None):
        super().__init__()
        self.theta = theta
        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    def get_params(self):
        return OrderedDict([
            ("theta", self.theta),
            ("n", self.n),
            ("taxa", self.n)
        ])

