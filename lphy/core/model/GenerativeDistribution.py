from abc import ABC, abstractmethod

from .Generator import Generator, get_generator_name
from ..parser.LPhyCanonicalBuilder import get_argument_lphy_string


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

    def generate(self) -> "Value":
        return self.sample()  # TODO how to pass id_

    def lphy_string(self):
        params = []
        for param_name, param in self.get_params():
            value = self.get_param(param_name)
            # if optional arg not used, it will be None
            if value is not None:
                params.append(f"{get_argument_lphy_string(param_name, value)}")

        code = f"{get_generator_name(self)}(" + ', '.join(params) + ")"
        return code

