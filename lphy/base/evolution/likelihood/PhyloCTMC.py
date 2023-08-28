from abc import ABC
from collections import OrderedDict

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class PhyloCTMC(GenerativeDistribution, ABC):

    def __init__(self, tree: Value, Q: Value, L=None, mu=None, site_rates=None, branch_rates=None, data_type=None):
        super().__init__()
        # have to take Value.value
        self.tree = tree.value
        self.Q = Q.value
        self.L = L.value if L is not None else None
        self.mu = mu.value if mu is not None else 1.0
        self.site_rates = site_rates.value if site_rates is not None else []
        self.branch_rates = branch_rates.value if branch_rates is not None else []
        self.data_type = data_type.value if data_type is not None else None

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    def get_params(self):
        return OrderedDict([
            ("tree", self.tree),
            ("Q", self.Q),
            ("L", self.L),
            ("mu", self.mu),
            ("siteRates", self.site_rates),
            ("branchRates", self.branch_rates),
            ("dataType", self.data_type)
        ])
