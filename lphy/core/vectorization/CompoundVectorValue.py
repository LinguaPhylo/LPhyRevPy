from typing import List
from abc import ABC, abstractmethod
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.vectorization import VectorUtils


def unwrap_values(values):
    return [value.value for value in values]


class CompoundVector(ABC):
    @abstractmethod
    def get_component_value(self, i) -> Value:
        pass


class CompoundVectorValue(Value, CompoundVector):

    def __init__(self, id, values: List[Value], function: DeterministicFunction):
        super().__init__(id, unwrap_values(values), function)
        self.component_values = values

    def set_id(self, id):
        super().set_id(id)
        for i, component_value in enumerate(self.component_values):
            component_value.set_id(f"{id}{VectorUtils.INDEX_SEPARATOR}{i}")

    def __str__(self):
        return f"{'' if self.is_anonymous() else f'{self.get_id()} = '}{str(self.value)}"

    def get_component_type(self):
        return self.value[0].__class__

    def get_component_value(self, i):
        return self.component_values[i]

    def get_component(self, i):
        return self.value[i]

    def size(self):
        return len(self.value)
