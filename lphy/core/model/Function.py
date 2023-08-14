from abc import ABC, abstractmethod

from .Generator import Generator


# TODO can this merge with DeterministicFunction?
class Function(Generator):
    from .ValueCollections import ValueDict
    param_map = ValueDict()

    def specification_operator(self):
        return '='

    def set_param(self, param_name: str, value: "Value"):
        self.param_map[param_name] = value

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

