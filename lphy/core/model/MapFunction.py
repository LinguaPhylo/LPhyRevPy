from typing import List

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.parser.argument.ArgumentValue import ArgumentValue


class MapFunction(DeterministicFunction):

    generator_info = {"name": "map",
                      "description": "A map defined by the argumentName=value pairs of its arguments."}

    def __init__(self, argument_objects: List[ArgumentValue]):
        super().__init__()
        # Create dict, key is argumentValue.name, value is argumentValue.value
        self.map = {argv.name: argv.value for argv in argument_objects}

    def apply(self) -> Value:
        return Value(None, self.map, self)



