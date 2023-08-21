from abc import ABC, abstractmethod

from .Generator import Generator


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

    def code_string(self):  # TODO
        map = self.get_params()
        iterator = iter(map.items())

        entry = next(iterator)

        builder = [f"{self.get_name()}({CodeStringUtils.getArgumentCodeString(entry)}"]

        for entry in iterator:
            builder.append(f", {CodeStringUtils.getArgumentCodeString(entry)}")

        builder.append(");")
        return ''.join(builder)
