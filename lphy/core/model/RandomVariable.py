from typing import List

from .GraphicalModelNode import GraphicalModelNode
from .Value import Value  # Import the base class


# RandomVariable generated from GenerativeDistribution
class RandomVariable(Value):
    from .GenerativeDistribution import GenerativeDistribution

    def __init__(self, value, id_: str, gen_dist: GenerativeDistribution):
        super().__init__(value, id_)
        self.gen_dist = gen_dist

    def get_generator(self):
        return self.gen_dist

    def get_generative_distribution(self):
        return self.gen_dist

    # an immutable list with a single element.
    def get_inputs(self) -> List[GraphicalModelNode]:
        return [self.gen_dist, ]
