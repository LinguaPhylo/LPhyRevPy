from typing import List

from .GraphicalModelNode import GraphicalModelNode
from .Value import Value  # Import the base class


class RandomVariable(Value):
    from .GenerativeDistribution import GenerativeDistribution

    def __init__(self, id_: str, value, gen_dist: GenerativeDistribution):
        super().__init__(id_, value)
        self.gen_dist = gen_dist

    def get_generator(self):
        return self.gen_dist

    def get_generative_distribution(self):
        return self.gen_dist

    def get_inputs(self) -> List[GraphicalModelNode]:
        return [self.gen_dist]
