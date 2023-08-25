from abc import ABC, abstractmethod

from .Generator import Generator


# TODO can this merge with DeterministicFunction?
class Function(Generator, ABC):
    from .ValueCollections import ValueDict
    param_map = ValueDict()

    def __init__(self, id_: str = None):
        super().__init__(id_)

    def specification_operator(self):
        return '='

    def set_param(self, param_name: str, value: "Value"):
        self.param_map[param_name] = value

    def get_params(self):
        return self.param_map

    def code_string(self):
        return CodeStringUtils.code_string(self, self.get_params())

    # TODO


class DeterministicFunction(Function, ABC):

    @abstractmethod
    def apply(self) -> "Value":
        pass

    def generate(self) -> "Value":
        return self.apply()

    def value(self) -> "Value":
        return self.apply().value()


    # TODO

