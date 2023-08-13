from abc import ABC, abstractmethod

from Generator import Generator
from Value import Value
from ValueCollections import ValueDict


# TODO can this merge with DeterministicFunction?
class Function(Generator):
    param_map = ValueDict()

    def set_param(self, param_name: str, value: Value):
        self.param_map[param_name] = value

    def specification_operator(self):
        return '='

    # TODO


class DeterministicFunction(Function, ABC):

    @abstractmethod
    def apply(self) -> Value:
        pass

    def generate(self) -> Value:
        return self.apply()

    def value(self) -> Value:
        return self.apply().value()

    def get_unique_id(self) -> str:
        return str(hash(self))

    # TODO

