from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value

from scipy import stats
from numpy import exp, zeros, sum

from lphy.core.parser.RevBuilder import get_argument_rev_string


# Developer guide:
# 1. argument names must be exactly same to lphy definition in @ParameterInfo
# 2. The field variable name to store Value objects must be same as its argument name, e.g. self.alpha = alpha,
#    which will be used for get_argument_rev_string(rev_name, value: Value),
#    in order to generate graphical model nodes recursively by lphy_to_rev(var_name).

# alphabetical order

class Beta(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        # keep Value objects for get_argument_rev_string(rev_name, value: Value)
        self.alpha = alpha
        self.beta = beta

        alpha_val = float(alpha.value)
        beta_val = float(beta.value)
        self.dist = stats.beta(alpha_val, beta_val)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return (f"""dnBeta({get_argument_rev_string("alpha", self.alpha)}, """ 
                f"""{get_argument_rev_string("beta", self.beta)})""")


class Binomial(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value, n: Value):
        super().__init__()
        self.p = p
        self.n = n

        self.p_val = float(self.p.value)  # the probability of a success
        self.n_val = float(self.n.value)  # number of trials
        # loc is the location of the distribution. offset?
        self.dist = stats.binom(self.n_val, self.p_val, loc=0)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        # Rev uses size not n
        return (f"""dnBinomial({get_argument_rev_string("p", self.p)}, """ 
                f"""{get_argument_rev_string("size", self.n)})""")


class Dirichlet(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, conc: Value):
        super().__init__()
        self.conc = conc
        if not isinstance(conc.value, list):
            raise ValueError(f"Expect list of concentration parameters for a Dirichlet distribution ! {conc.value}")
        if not all(isinstance(element, (int, float)) for element in conc.value):
            raise ValueError(
                f"The concentration parameters for a Dirichlet distribution must be numbers ! {conc.value}")
        self.conc_val = self.conc.value

    def sample(self, id_: str = None) -> RandomVariable:
        dirichlet = zeros(len(self.conc_val))

        for i in range(len(dirichlet)):
            dirichlet[i] = stats.gamma.rvs(float(self.conc_val[i]), scale=1.0, size=1)
        dirichlet /= sum(dirichlet)

        return RandomVariable(id_, dirichlet, self)

    def density(self, t):
        raise UnsupportedOperationException("TODO")

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        return f"""dnDirichlet({get_argument_rev_string("alpha", self.conc)})"""


class Cauchy(GenerativeDistribution):
    pass  # TODO


class Exp(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value):
        super().__init__()
        self.mean = mean

        self.mean_val = float(self.mean.value)
        # scale = 1 / lambda, where lambda is the rate parameter
        self.dist = stats.expon(scale=self.mean_val)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        # TODO cannot use get_argument_rev_string for rate
        # Rev lambda : The rate ( rate==1/mean) parameter. Default : 1
        rate = 1 / self.mean_val
        return f"dnExp(lambda={rate})"


class Gamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, scale: Value):
        super().__init__()
        self.shape = shape
        self.scale = scale

        self.shape_val = float(self.shape.value)
        self.scale_val = float(self.scale.value)

        self.dist = stats.gamma(self.shape_val, scale=self.scale_val)

    def sample(self, id_: str = None) -> RandomVariable:
        # rvs(a, loc=0, scale=1, size=1) where a is shape
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        # TODO cannot use get_argument_rev_string for rate
        rate = 1 / self.scale_val
        return (f"""dnGamma({get_argument_rev_string("shape", self.shape)}, """ 
                f"""rate={rate}""")


class InverseGamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        self.alpha = alpha
        self.beta = beta

        self.alpha_val = float(self.alpha.value)
        # a rate parameter, also called inverse scale parameter, beta = 1 / scale
        self.beta_val = float(self.beta.value)
        scale = 1 / self.beta_val
        # Create an Inverse Gamma distribution object
        self.dist = stats.invgamma(self.alpha_val, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        # Generate random numbers from the Inverse Gamma distribution
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return (f"""dnInverseGamma({get_argument_rev_string("shape", self.alpha)}, """ 
                f"""{get_argument_rev_string("rate", self.beta)})""")


class Normal(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, sd: Value):
        super().__init__()
        self.mean = mean
        self.sd = sd

        self.mean_val = float(self.mean.value)
        self.sd_val = float(self.sd.value)
        # loc is mean and scale is standard deviation of the normal distribution
        self.dist = stats.norm(loc=self.mean_val, scale=self.sd_val)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    # TODO: x <- rnorm(n=10,mean=5,sd=10)
    def lphy_to_rev(self, var_name):
        return (f"""dnNormal({get_argument_rev_string("mean", self.mean)}, """ 
                f"""{get_argument_rev_string("sd", self.sd)})""")


# Multivariate Normal distribution.
class MVN(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, covariances: Value):
        super().__init__()
        raise UnsupportedOperationException(" in dev !")
        self.mean = mean
        self.covariances = covariances
        self.mean_arr = mean.value
        # TODO how to deal with matrix here?
        self.covariances_arr = covariances.value

        self.dist = stats.multivariate_normal(mean=self.mean_arr, cov=self.covariances_arr)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        # TODO check
        # Rev mean : Real[] (pass by const reference). The vector of mean values.
        # covariance :	MatrixRealSymmetric (pass by const reference). The variance-covariance matrix. Default : NULL
        return (f"""dnMultivariateNormal({get_argument_rev_string("mean", self.mean)}, """ 
                f"""{get_argument_rev_string("covariances", self.covariances)})""")


class LogNormal(GenerativeDistribution):

    def __init__(self, meanlog: Value, sdlog: Value, offset: Value = None):
        super().__init__()
        # keep Value objects for get_argument_rev_string(rev_name, value: Value)
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset # optional, could be None

        self.meanlog_val = float(self.meanlog.value)
        self.sdlog_val = float(self.sdlog.value)
        if offset is not None: #TODO
            raise UnsupportedOperationException("Rev language does not support offset in dnLognormal !")

        # TODO check, not sure if correct !!!
        # Suppose a normally distributed random variable X has mean mu and standard deviation sigma.
        # Then Y = exp(X) is lognormally distributed with s = sigma and scale = exp(mu).
        scale = exp(self.meanlog_val)
        self.dist = stats.lognorm(self.sdlog_val, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1) + self._C()
        return RandomVariable(id_, x, self)

    def log_density(self, x):
        return self.dist.logpdf(x - self._C(), self.sdlog_val, scale=exp(self.meanlog_val))

    def _C(self):
        return float(self.offset.value) if self.offset is not None else 0.0

    def lphy_to_rev(self, var_name):
        # Rev mean in log-space (observed mean is exp(m)).
        # sd, standard deviation, also in log-space.
        return (f"""dnLognormal({get_argument_rev_string("mean", self.meanlog)}, """ 
                f"""{get_argument_rev_string("sd", self.sdlog)})""")


class Uniform(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, lower: Value, upper: Value):
        super().__init__()
        self.lower = lower
        self.upper = upper

        self.lower_val = float(self.lower.value)
        self.upper_val = float(self.upper.value)
        # loc is the lower boundary of the output interval.
        # Upper boundary of the output interval will be (loc + scale). Must be non-negative.
        scale = self.lower_val + self.upper_val
        self.dist = stats.uniform(loc=self.lower_val, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return (f"""dnUniform({get_argument_rev_string("lower", self.lower)}, """ 
                f"""{get_argument_rev_string("upper", self.upper)})""")
