from abc import ABC, abstractmethod
import math
from .Generator import Generator, get_generator_name


class GenerativeDistribution(Generator, ABC):

    def __init__(self, id_: str = None):
        super().__init__(id_)

    def specification_operator(self):
        return '~'

    def rev_spec_op(self) -> str:
        return '~'

    # TODO rename to create_var_by_id
    @abstractmethod
    def sample(self, id_: str = None) -> "RandomVariable":
        pass

    # must overwrite either this or log_density
    def density(self, t):
        return math.exp(t.log_density())

    def log_density(self, t):
        return math.log(t.density())

    def generate(self) -> "Value":
        return self.sample()  # TODO how to pass id_

    def lphy_string(self):
        from lphy.core.parser.LPhyCanonicalBuilder import get_argument_lphy_string
        params = []
        for param_name, param in self.get_params():
            value = self.get_param(param_name)
            # if optional arg not used, it will be None
            if value is not None:
                params.append(f"{get_argument_lphy_string(param_name, value)}")

        code = f"{get_generator_name(self)}(" + ', '.join(params) + ")"
        return code
