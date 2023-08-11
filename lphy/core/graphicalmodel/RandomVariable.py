from typing import List
from Value import Value  # Import the base class
from core.graphicalmodel.GenerativeDistribution import GenerativeDistribution
from core.graphicalmodel.GraphicalModelNode import GraphicalModelNode


class RandomVariable(Value):

    def __init__(self, id_: str, value, gen_dist: GenerativeDistribution):
        super().__init__(id_, value)
        self.gen_dist = gen_dist

    def get_generator(self):
        return self.gen_dist

    def get_generative_distribution(self):
        return self.gen_dist

    def get_inputs(self) -> List[GraphicalModelNode]:
        return [self.gen_dist]
