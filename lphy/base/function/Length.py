from abc import ABC
from lphy.core.model.Function import DeterministicFunction, method_info
from lphy.core.model.Value import Value


class Length(DeterministicFunction, ABC):
    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "length",
                      "description": "the length of the given argument"}

    def __init__(self, arg_0: Value):
        super().__init__()
        # deal with None later
        self.arg_0 = arg_0

    def apply(self) -> "Value":
        length = 1
        v = self.arg_0
        if v is not None and isinstance(v.value, list):
            length = len(v.value)
        return Value(None, length, self)

    def lphy_to_rev(self, var_name):
        if self.arg_0 is None:
            raise ValueError("Cannot pass None to the function length !")

        # this is generalised to handle Slice, e.g. length(z[0])
        sup_str = super().lphy_to_rev(var_name)
        # then use regx to convert to rev
        # [^)] means "match any character except the closing parenthesis )."
        pattern = r'length\(([^)]+)\)'
        replacement = r'\1.size()'
        import re
        output_string = re.sub(pattern, replacement, sup_str)
        return output_string

