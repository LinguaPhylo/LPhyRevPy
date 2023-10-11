from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


### alphabetical order

class Beta(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, alpha: Value, beta: Value):
        super().__init__()
        self.alpha = alpha
        self.beta = beta

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

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
        # not need value
        return RandomVariable(id_, None, self)

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
        # not need value
        return RandomVariable(id_, None, self)

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
        # not need value
        return RandomVariable(id_, None, self)

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
        # not need value
        return RandomVariable(id_, None, self)

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
        if offset is not None:
            raise UnsupportedOperationException("Rev language does not support offset in dnLognormal !")

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    # x ~ dnLognormal(mean=mean, sd=sd)
    def lphy_to_rev(self, var_name):
        # TODO no offset ?
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
        # not need value
        return RandomVariable(id_, None, self)

    def lphy_to_rev(self, var_name):
        lower = self.lower.value
        upper = self.upper.value
        return f"dnUniform(lower={lower}, upper={upper})"

