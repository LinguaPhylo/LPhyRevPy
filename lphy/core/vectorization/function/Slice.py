from abc import ABC
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class Slice(DeterministicFunction, ABC):

    def __init__(self, start: Value, end: Value, array: Value):
        super().__init__()
        self.start = start
        self.end = end
        self.array = array

    def apply(self):#TODO
        if self.end > self.start:
            new_array = self.array[self.start:self.end + 1]
        else:
            new_array = self.array[self.start]
        return new_array

    def lphy_to_rev(self, var_name):
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("TODO")


    def lphy_string(self):
        array_string = self.array.codeString() if not self.array.isAnonymous() else self.array.getId()
        start_string = str(self.start)
        end_string = str(self.end)

        if not start_string.isAnonymous() or not end_string.isAnonymous():
            return super().codeString()

        if start_string == end_string:
            return f"{array_string}[{start_string}]"

        return f"{array_string}[{start_string}:{end_string}]"

    def size(self):
        return self.end - self.start + 1
