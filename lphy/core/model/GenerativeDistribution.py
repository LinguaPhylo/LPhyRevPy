from abc import ABC, abstractmethod

from .Generator import Generator, get_generator_name, get_argument_code_string


class GenerativeDistribution(Generator, ABC):

    def __init__(self, id_: str = None):
        super().__init__(id_)

    def specification_operator(self):
        return '~'

    # TODO rename to create_var_by_id
    @abstractmethod
    def sample(self, id_: str = None) -> "RandomVariable":
        pass

    def generate(self) -> "Value":
        return self.sample()  # TODO how to pass id_

#TODO use attr now
    # This must be overwritten if the func/dist name not same as the class name, case-sensitive.
    # def get_name(self) -> str:
    #     return type(self).__name__

    def code_string(self):
        params = []
        for param_name, param in self.get_params():
            value = self.get_param(param_name)
            # if optional arg not used, it will be None
            if value is not None:
                params.append(f"{get_argument_code_string(param_name, value)}")

        code = f"{get_generator_name(self)}(" + ', '.join(params) + ");"
        return code

