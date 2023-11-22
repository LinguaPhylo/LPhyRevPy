from typing import List

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.vectorization import VectorUtils
from lphy.core.vectorization.CompoundVectorValue import CompoundVector


def unwrap_values(values: List[RandomVariable]):
    return [value.value for value in values]


class VectorizedRandomVariable(RandomVariable, CompoundVector):

    def __init__(self, id_: str, component_variables: List[RandomVariable],
                 generative_distribution: GenerativeDistribution):
        super().__init__(id_, unwrap_values(component_variables), generative_distribution)
        self.component_variables = []
        for i in range(len(self.value())):
            self.component_variables.append(component_variables[i])

    def set_id(self, id: str):
        super().set_id(id)
        for i in range(len(self.component_variables)):
            self.component_variables[i].set_id(f"{id}{VectorUtils.INDEX_SEPARATOR}{i}")

    def get_component_type(self):
        return self.value()[0].getClass()

    def get_component(self, i: int):
        return self.value()[i]

    def size(self) -> int:
        return len(self.value())

    def get_component_value(self, i: int) -> RandomVariable:
        return self.component_variables[i]
