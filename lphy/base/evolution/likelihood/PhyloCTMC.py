from abc import ABC
from core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class PhyloCTMC(GenerativeDistribution, ABC):

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, tree: Value, Q: Value, L=None, mu=None, siteRates=None, branchRates=None, dataType=None):
        super().__init__()
        # have to take Value.value
        self.tree = tree
        self.Q = Q
        self.L = L
        self.mu = mu if mu is not None else Value(None, 1.0)
        self.siteRates = siteRates
        self.branchRates = branchRates
        self.dataType = dataType

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)


    def lphy_to_rev(self):
        # lphy names are same to rev
        tree_name = "tree"
        tree = self.get_param(tree_name)
        q_name = "Q"
        q = self.get_param(q_name)

        builder = [get_argument_rev_string(tree_name, tree), get_argument_rev_string(q_name, q)]
        #TODO optional
        # lphy name diff to rev
        if self.L is not None:
            l = self.get_param("L")
            builder.append(get_argument_rev_string("nSites", l))
        if self.dataType is not None:
            data_type = self.get_param("dataType")
            builder.append(get_argument_rev_string("type", data_type))

        args = ", ".join(builder)
        return f"dnPhyloCTMC({args})"

