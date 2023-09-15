from abc import ABC
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value

class ElementsAt(DeterministicFunction, ABC):

    def __init__(self, index: Value, array: Value):
        super().__init__()
        self.index = index
        self.array = array

    def apply(self):
        index = self.index
        array = self.array

        if len(index) > 1:
            new_array = array[index]
        else:
            new_array = array[index[0]]
        return new_array

    def lphy_to_rev(self, var_name):
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("TODO")


    def lphy_string(self):
        array_string = self.array.codeString() if not self.array.isAnonymous() else self.array.getId()
        index_string = str(self.index) if not self.index.isAnonymous() else self.index.getId()

        if not self.index.isAnonymous():
            return super().codeString()

        return f"{array_string}[{index_string}]"
