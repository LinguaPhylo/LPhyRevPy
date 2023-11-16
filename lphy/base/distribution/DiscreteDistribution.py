from typing import List

import numpy as np
from numpy import zeros
from scipy import stats

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
        # keep Value objects for get_argument_rev_string(rev_name, value: Value)
        self.shape = shape
        self.ncat = ncat
        # create distribution
        self.shape_val = float(shape.value)
        self.ncat_val = int(ncat.value)
        self.dist = stats.gamma(self.shape_val, scale=1.0 / self.shape_val)

    def sample(self, id_: str = None) -> RandomVariable:
        rates = zeros(self.ncat_val)
        for i in range(self.ncat_val):
            q = (2.0 * i + 1.0) / (2.0 * self.ncat_val)
            rates[i] = self.dist.ppf(q)
        # Java between 0 (inclusive) and n (exclusive).
        # Here range [a, b], including both end points
        cat_index = random.randint(0, self.ncat_val - 1)

        return RandomVariable(id_, rates[cat_index], self)

    def density(self, t):
        raise UnsupportedOperationException("TODO")

    # sr := fnDiscretizeGamma( alpha, alpha, 4 )
    def rev_spec_op(self) -> str:
        return ':='

    # Note: fnDiscretizeGamma is diff to DiscretizeGamma, the former returns the category rates, length == ncat,
    # but the latter returns the rate for one site, use IID to return site rates.
    def lphy_to_rev(self, var_name):
        return (f"""fnDiscretizeGamma({get_argument_rev_string("shape", self.shape)}, """
                f"""{get_argument_rev_string("rate", self.shape)}, """
                f"""{get_argument_rev_string("numCats", self.ncat)})""")


# TODO ignore replicates=L in DiscretizeGamma, or better solution?

### alphabetical order

class Bernoulli(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p  # the probability of success.
        self.p_val = float(self.p.value)

    def sample(self, id_: str = None) -> RandomVariable:
        success = random.random() < self.p_val
        return RandomVariable(id_, success, self)

    def density(self, success):
        return self.p_val if success else 1.0 - self.p_val

    def lphy_to_rev(self, var_name):
        return f"""dnBernoulli({get_argument_rev_string("p", self.p)}"""


def categorical_sample(probs: List, rand_num):
    # Create cumulative probability distribution
    cum_prob = np.cumsum(probs)
    # returned index `i` satisfies: ``a[i-1] < v <= a[i]``
    return np.searchsorted(cum_prob, rand_num, side="left")


class Categorical(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p  # the probability distribution over integer states 1 to K.
        if not isinstance(p.value, list):
            raise ValueError(f"Expect list of  probability for each category ! {p.value}")
        self.p_list = self.p.value

    def sample(self, id_: str = None) -> RandomVariable:
        rand_num = random.random()
        i = categorical_sample(self.p_list, rand_num)
        return RandomVariable(id_, i, self)

    def lphy_to_rev(self, var_name):
        return f"""dnCat({get_argument_rev_string("p", self.p)}"""


class Geometric(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value):
        super().__init__()
        self.p = p # the probability of success.
        self.p_val = float(self.p.value)

        self.dist = stats.geom(self.p_val)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return f"""dnGeometric({get_argument_rev_string("p", self.p)}"""


class Poisson(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    # lambda is reserved by python
    def __init__(self, lambda_: Value, min=None, max=None, offset=None):
        super().__init__()
        self.lambda_ = lambda_  # the expected number of events.
        self.lambda_val = float(self.lambda_.value)
        if min is not None or max is not None:
            raise UnsupportedOperationException("Rev language does not support a condition in dnPoisson !")
        self.offset = offset  # optional, could be None

        self.dist = stats.poisson(mu=self.lambda_val)

    def sample(self, id_: str = None) -> RandomVariable:
        # Rev do not support min and max
        # while val < minimum_value or val > maximum_value:
        x = self.dist.rvs(size=1) + self._C()
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        lambda_ = self.lambda_.value
        return f"""dnPoisson({get_argument_rev_string("lambda", self.lambda_)}"""

    def _C(self) -> int:
        return int(self.offset.value) if self.offset is not None else 0


# The discrete uniform distribution over integers.
class UniformDiscrete(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, lower: Value, upper: Value):
        super().__init__()
        self.lower = lower  # the lower bound (inclusive) of the uniform distribution on integers.
        self.upper = upper  # the upper bound (inclusive) of the uniform distribution on integers.

        self.lower_val = int(self.lower.value)
        self.upper_val = int(self.upper.value)

    def sample(self, id_: str = None) -> RandomVariable:
        # Return random integer in range [a, b], including both end points.
        x = random.randint(self.lower_val, self.upper_val)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return (f"""dnUniformInteger({get_argument_rev_string("lower", self.lower)}, """ 
                f"""{get_argument_rev_string("upper", self.upper)})""")
