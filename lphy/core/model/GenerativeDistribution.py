from abc import ABC, abstractmethod

from .Generator import Generator


class GenerativeDistribution(Generator, ABC):

    def specification_operator(self):
        return '~'

    # TODO rename to create_var_by_id
    @abstractmethod
    def sample(self, id_: str = None) -> "RandomVariable":
        pass

    def generate(self) -> "Value":
        return self.sample() # TODO how to pass id_
