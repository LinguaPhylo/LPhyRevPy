from abc import ABC, abstractmethod

from .Generator import Generator


def _get_argument_code_string(name, value):
    prefix = ""
    if not name.isdigit():  # Assuming ExpressionUtils.isInteger(name) is equivalent to name.isdigit()
        prefix = name + "="

    if value is None:
        raise RuntimeError("Value of " + name + " is None!")

    if value.is_anonymous():
        return prefix + value.code_string()
    return prefix + value.get_id()


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

    # This must be overwritten if the func/dist name not same as the class name, case-sensitive.
    def get_name(self) -> str:
        return type(self).__name__

    def code_string(self):
        params = []
        for key, value in self.get_params().items():
            params.append(f"{_get_argument_code_string(key, value)}")

        code = f"{self.get_name()}(" + ', '.join(params) + ");"
        return code

