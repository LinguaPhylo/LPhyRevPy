from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class Coalescent(GenerativeDistribution):
    # TODO bug the arg_value not matching the correct order, n <- taxa, for Coalescent(theta=Θ, taxa=taxa);
    def __init__(self, theta: Value, n: Value = None, taxa: Value = None):
        if (n is not None and taxa is not None) or (n is None and taxa is None):
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")

        super().__init__()
        self.theta = theta
        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> "RandomVariable":
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self):
        theta = self.theta.value
        if self.taxa is not None:
            taxa = self.taxa.value
            return f"dnCoalescent(theta={theta}, taxa={taxa});"
        elif self.n is not None:
            n = self.n.value
            from lphy.core.error.Errors import UnsupportedOperationException
            raise UnsupportedOperationException("TODO !")
        else:
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")
