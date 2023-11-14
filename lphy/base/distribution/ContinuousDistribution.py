from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value

from scipy.stats import beta, lognorm, gamma, norm, uniform, expon
from numpy import exp, sqrt, zeros, sum


### alphabetical order

class Beta(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        self.alpha = alpha
        self.beta = beta

    def sample(self, id_: str = None) -> RandomVariable:
        alpha = float(self.alpha.value)
        beta_ = float(self.beta.value)
        x = beta.rvs(alpha, beta_, size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        alpha = self.alpha
        beta = self.beta
        return f"dnBeta(alpha={alpha}, beta={beta})"


class Binomial(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, p: Value, n: Value):
        super().__init__()
        self.p = p
        self.n = n

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        p = self.p
        n = self.n
        # Rev uses size not n
        return f"dnBinomial(p={p}, size={n})"


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
        conc = self.conc.value
        dirichlet = zeros(len(conc))

        for i in range(len(dirichlet)):
            dirichlet[i] = gamma.rvs(float(conc[i]), scale=1.0, size=1)
        dirichlet /= sum(dirichlet)

        return RandomVariable(id_, dirichlet, self)

    def density(self, t):
        raise UnsupportedOperationException("TODO")

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        conc = self.conc.value
        return f"dnDirichlet(alpha={conc})"


class Cauchy(GenerativeDistribution):
    pass


class Exp(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value):
        super().__init__()
        self.mean = mean

    def sample(self, id_: str = None) -> RandomVariable:
        mean = float(self.mean.value)
        # scale = 1 / lambda, where lambda is the rate parameter
        x = expon.rvs(scale=mean, size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        mean = self.mean.value
        rate = 1 / float(mean)
        return f"dnExp(lambda={rate})"


class Gamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, scale: Value):
        super().__init__()
        self.shape = shape
        self.scale = scale

    def sample(self, id_: str = None) -> RandomVariable:
        shape = float(self.shape.value)
        scale = float(self.scale.value)
        # rvs(a, loc=0, scale=1, size=1) where a is shape
        x = beta.rvs(shape, scale=scale, size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        shape = self.shape.value
        scale = self.scale.value
        rate = 1 / float(scale)
        return f"dnGamma(shape={shape}, rate={rate})"


class InverseGamma(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, shape: Value, scale: Value):
        super().__init__()
        self.shape = shape
        self.scale = scale

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        shape = self.shape.value
        scale = self.scale.value
        rate = 1 / float(scale)
        return f"dnInverseGamma(shape={shape}, rate={rate})"


class Normal(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, sd: Value):
        super().__init__()
        self.mean = mean
        self.sd = sd

    def sample(self, id_: str = None) -> RandomVariable:
        mean = float(self.mean.value)
        sd = float(self.sd.value)
        # loc is mean and scale is standard deviation of the normal distribution
        x = norm.rvs(loc=mean, scale=sd, size=1)
        return RandomVariable(id_, x, self)

    # TODO: x <- rnorm(n=10,mean=5,sd=10)
    def lphy_to_rev(self, var_name):
        mean = self.mean.value
        sd = self.sd.value
        return f"dnNormal(mean={mean}, sd={sd})"


class MVN(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, mean: Value, covariances: Value):
        super().__init__()
        self.mean = mean
        #TODO matrix here
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
    def __init__(self, meanlog: Value, sdlog: Value, offset=None):
        super().__init__()
        self.meanlog = meanlog
        self.sdlog = sdlog
        self.offset = offset
        if offset is not None:
            raise UnsupportedOperationException("Rev language does not support offset in dnLognormal !")

    def sample(self, id_: str = None) -> RandomVariable:
        meanlog = float(self.meanlog.value)
        sdlog = float(self.sdlog.value)
        # TODO check, not sure if correct !!!
        # Suppose a normally distributed random variable X has mean mu and standard deviation sigma.
        # Then Y = exp(X) is lognormally distributed with s = sigma and scale = exp(mu).
        s = float(sdlog)
        scale = exp(float(meanlog))
        y = lognorm.rvs(s, scale=scale, size=1) + self._C()
        return RandomVariable(id_, y, self)

    def log_density(self, x):
        meanlog = self.meanlog.value
        sdlog = self.sdlog.value

        return lognorm.logpdf(x - self._C(), float(sdlog), scale=exp(float(meanlog)))

    def _C(self):
        C = 0.0
        if self.offset is not None:
            C = float(self.offset.value)
        return C

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        mean = self.meanlog.value
        sd = self.sdlog.value
        return f"dnLognormal(mean={mean}, sd={sd})"


class Uniform(GenerativeDistribution):
    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, lower: Value, upper: Value):
        super().__init__()
        self.lower = lower
        self.upper = upper

    def sample(self, id_: str = None) -> RandomVariable:
        # loc is the lower boundary of the output interval.
        loc = float(self.lower.value)
        # Upper boundary of the output interval will be (loc + scale). Must be non-negative.
        scale = loc + float(self.upper.value)
        x = uniform.rvs(loc=loc, scale=scale, size=1)
        return RandomVariable(id_, x, self)

    def lphy_to_rev(self, var_name):
        lower = self.lower.value
        upper = self.upper.value
        return f"dnUniform(lower={lower}, upper={upper})"

