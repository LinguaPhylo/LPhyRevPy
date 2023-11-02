from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class BirthDeathSerialSampling(GenerativeDistribution):
    """
    A tree of extant species and those sampled through time, which is conceptually embedded
    in a full species tree produced by a speciation-extinction (birth-death) branching process.
    Conditioned on root age and on number of taxa and their ages (Stadler and Yang, 2013).
    """
    def __init__(self, lambda_: Value, mu: Value, rho: Value, psi: Value,
                 n: Value = None, taxa: Value = None, ages: Value = None, rootAge: Value = None):
        # this is more restrict, to avoid requiring extra Rev code to create taxa
        if (ages is not None and taxa is not None) or (ages is None and taxa is None):
            raise ValueError("Either 'taxa' or 'ages' should be provided to 'BirthDeathSerialSampling', but not both !")

        super().__init__()
        self.lambda_ = lambda_ # TODO lambda is reserved by python
        self.mu = mu
        self.rho = rho
        self.psi = psi

        self.n = n
        self.taxa = taxa
        self.ages = ages
        self.rootAge = rootAge

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    def lphy_to_rev(self, var_name):
        #TODO
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("in dev !")
        # lphy names are same to rev
        theta_name = "theta"
        taxa_name = "taxa"
        theta = self.get_param(theta_name)
        if self.taxa_obj is not None:
            taxa = self.get_param(taxa_name)
            #TODO https://revbayes.github.io/documentation/dnBirthDeathSamplingTreatment.html
            return f"dnBDSTP({get_argument_rev_string(theta_name, theta)}, {get_argument_rev_string(taxa_name, taxa)})"
        elif self.n is not None:
            n = self.n.value

            raise UnsupportedOperationException("TODO !")
        else:
            raise ValueError("Either 'n' or 'taxa' should be provided to 'BirthDeathSerialSampling', but not both or neither !")
