from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value

from scipy import stats
from numpy import exp, sqrt, zeros, sum


# alphabetical order

class Beta(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        self.alpha = float(alpha.value)
        self.beta = float(beta.value)

        self.dist = stats.beta(self.alpha, self.beta)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return f"dnBeta(alpha={self.alpha}, beta={self.beta})"


class Binomial(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value, n: Value):
        super().__init__()
        self.p = float(p.value)  # the probability of a success
        self.n = float(n.value)  # number of trials
        # loc is the location of the distribution. offset?
        self.dist = stats.binom(self.n, self.p, loc=0)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        # Rev uses size not n
        return f"dnBinomial(p={self.p}, size={self.n})"


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

    def sample(self, id_: str = None) -> RandomVariable:
        conc_val = self.conc.value
        dirichlet = zeros(len(conc_val))

        for i in range(len(dirichlet)):
            dirichlet[i] = stats.gamma.rvs(float(conc_val[i]), scale=1.0, size=1)
        dirichlet /= sum(dirichlet)

        return RandomVariable(id_, dirichlet, self)

    def density(self, t):
        raise UnsupportedOperationException("TODO")

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        conc_val = self.conc.value
        return f"dnDirichlet(alpha={conc_val})"


class Cauchy(GenerativeDistribution):
    pass #TODO


class Exp(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value):
        super().__init__()
        self.mean = float(mean.value)
        # scale = 1 / lambda, where lambda is the rate parameter
        self.dist = stats.expon(scale=self.mean)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        rate = 1 / float(self.mean)
        return f"dnExp(lambda={rate})"


class Gamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, scale: Value):
        super().__init__()
        self.shape = float(shape.value)
        self.scale = float(scale.value)

        self.dist = stats.gamma(self.shape, scale=self.scale)

    def sample(self, id_: str = None) -> RandomVariable:
        # rvs(a, loc=0, scale=1, size=1) where a is shape
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        rate = 1 / float(self.scale)
        return f"dnGamma(shape={self.shape}, rate={rate})"


class InverseGamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        self.alpha = float(alpha.value)
        # a rate parameter, also called inverse scale parameter, beta = 1 / scale
        self.beta = float(beta.value)
        scale = 1 / self.beta
        # Create an Inverse Gamma distribution object
        self.dist = stats.invgamma(self.alpha, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        # Generate random numbers from the Inverse Gamma distribution
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return f"dnInverseGamma(shape={self.alpha}, rate={self.beta})"


class Normal(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, sd: Value):
        super().__init__()
        self.mean = float(mean.value)
        self.sd = float(sd.value)
        # loc is mean and scale is standard deviation of the normal distribution
        self.dist = stats.norm(loc=self.mean, scale=self.sd)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    # TODO: x <- rnorm(n=10,mean=5,sd=10)
    def lphy_to_rev(self, var_name):
        return f"dnNormal(mean={self.mean}, sd={self.sd})"


class MVN(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, covariances: Value):
        super().__init__()
        self.mean = mean
        # TODO matrix here
        self.covariances = covariances

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        mean = self.mean.value
        covariances = self.covariances.value
        # TODO matrix here
        return f"dnMultivariateNormal(mean={mean}, covariances={covariances})"


class LogNormal(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, meanlog: Value, sdlog: Value, offset: Value = None):
        super().__init__()
        self.meanlog = float(meanlog.value)
        self.sdlog = float(sdlog.value)
        if offset is not None:
            raise UnsupportedOperationException("Rev language does not support offset in dnLognormal !")
        # optional, could be None
        self.offset = float(offset.value) if offset is not None else None

        # TODO check, not sure if correct !!!
        # Suppose a normally distributed random variable X has mean mu and standard deviation sigma.
        # Then Y = exp(X) is lognormally distributed with s = sigma and scale = exp(mu).
        scale = exp(self.meanlog)
        self.dist = stats.lognorm(self.sdlog, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1) + self._C()
        return RandomVariable(id_, x, self)

    def log_density(self, x):
        return self.dist.logpdf(x - self._C(), self.sdlog, scale=exp(self.meanlog))

    def _C(self):
        return self.offset if self.offset is not None else 0.0

    def lphy_to_rev(self, var_name):
        # Rev mean in log-space (observed mean is exp(m)).
        # sd, standard deviation, also in log-space.
        return f"dnLognormal(mean={self.meanlog}, sd={self.sdlog})"


class Uniform(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, lower: Value, upper: Value):
        super().__init__()
        self.lower = float(lower.value)
        self.upper = float(upper.value)
        # loc is the lower boundary of the output interval.
        # Upper boundary of the output interval will be (loc + scale). Must be non-negative.
        scale = self.lower + self.upper
        self.dist = stats.uniform(loc=self.lower, scale=scale)

    def sample(self, id_: str = None) -> RandomVariable:
        x = self.dist.rvs(size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        return f"dnUniform(lower={self.lower}, upper={self.upper})"
