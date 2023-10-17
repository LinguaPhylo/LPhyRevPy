from numpy import zeros
from scipy.stats import gamma

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.parser.RevBuilder import get_argument_rev_string

import random


# This is also for Site Model.
class DiscretizeGamma(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, ncat: Value):
        super().__init__()
        self.shape = shape
        self.ncat = ncat

    def sample(self, id_: str = None) -> RandomVariable:
        shape = self.shape.value
        ncat = int(self.ncat.value)

        sh = float(shape)
        gamma_distribution = gamma(sh, scale=1.0 / sh)

        rates = zeros(ncat)
        for i in range(ncat):
            q = (2.0 * i + 1.0) / (2.0 * ncat)
            rates[i] = gamma_distribution.ppf(q)
        # Java between 0 (inclusive) and n (exclusive).
        # Here range [a, b], including both end points
        cat_index = random.randint(0, ncat-1)

        return RandomVariable(id_, rates[cat_index], self)

    def density(self, t):
        raise UnsupportedOperationException("TODO")

    # sr := fnDiscretizeGamma( alpha, alpha, 4 )
    def rev_spec_op(self) -> str:
        return ':='

    # Note: fnDiscretizeGamma is diff to DiscretizeGamma, the former returns the category rates, length == ncat,
    # but the latter returns the rate for one site, use IID to return site rates.
    def lphy_to_rev(self, var_name):
        shape_name = "shape"
        rate_name = "rate"
        ncat_name = "numCats"
        shape = self.get_param(shape_name)
        ncat = self.get_param("ncat")
        return (f"fnDiscretizeGamma({get_argument_rev_string(shape_name, shape)}, "
                f"{get_argument_rev_string(rate_name, shape)}, "
                f"{get_argument_rev_string(ncat_name, ncat)})")


# TODO ignore replicates=L in DiscretizeGamma, or better solution?

### alphabetical order

class Bernoulli(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p

    def sample(self, id_: str = None) -> RandomVariable:
        success = random.random() < self.p.value
        return RandomVariable(id_, success, self)

    def density(self, success):
        p = self.p.value
        return float(p) if success else 1.0 - float(p)

    def lphy_to_rev(self, var_name):
        p = self.p.value
        return f"dnBernoulli(p={p})"


class Categorical(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p
        if not isinstance(p.value, list):
            raise ValueError(f"Expect list of  probability for each category ! {p.value}")

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        #TODO p shoud be array here
        p = self.p.value
        return f"dnCat(p={p})"


class Geometric(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        p = self.p.value
        return f"dnGeometric(p={p})"


class Poisson(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    # lambda is reserved by python
    def __init__(self, lambda_: Value, min=None, max=None, offset=None):
        super().__init__()
        self.lambda_ = lambda_
        if min is not None or max is not None:
            raise UnsupportedOperationException("Rev language does not support a condition in dnPoisson !")
        if offset is not None:
            raise UnsupportedOperationException("Rev language does not support offset in dnPoisson !")

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        lambda_ = self.lambda_.value
        return f"dnPoisson(lambda={lambda_})"


class UniformDiscrete(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, lower: Value, upper: Value):
        super().__init__()
        self.lower = lower
        self.upper = upper

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        lower = self.lower.value
        upper = self.upper.value
        return f"dnUniformInteger(lower={lower}, upper={upper})"
