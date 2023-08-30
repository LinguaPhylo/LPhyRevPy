from abc import ABC
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class PhyloCTMC(GenerativeDistribution, ABC):

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, tree: Value, Q: Value, L=None, mu=None, site_rates=None, branch_rates=None, data_type=None):
        super().__init__()
        # have to take Value.value
        self.tree = tree
        self.Q = Q
        self.L = L if L is not None else None
        self.mu = mu if mu is not None else Value(None, 1.0)
        self.site_rates = site_rates
        self.branch_rates = branch_rates
        self.data_type = data_type

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)


    def lphy_to_rev(self):
        pass

