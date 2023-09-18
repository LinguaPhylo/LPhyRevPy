from abc import ABC
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class Slice(DeterministicFunction, ABC):
    generator_info = {"name": "slice",
                      "description": "A function to slice a subarray from an array."}

    def __init__(self, start: Value, end: Value, array: Value):
        super().__init__()
        self.start = start
        self.end = end
        self.array = array  # array (list) to retrieve element of

    def apply(self):
        s = int(self.start.value)
        e = int(self.end.value)
        arr = self.array.value

        if e > s:
            new_array = arr[s:(e + 1)]
        else:
            new_array = arr[s]
        return Value(None, new_array, self)

    def lphy_to_rev(self, var_name):
        #TODO why Java code needs: self.array.lphy_to_rev(var_name) if not self.array.is_anonymous() else self.array.get_id()
        array_string = self.array.get_id()
        start_string = self.start.lphy_to_rev(var_name)
        end_string = self.end.lphy_to_rev(var_name)

        if not self.start.is_anonymous() or not self.end.is_anonymous():
            return super().lphy_to_rev(var_name)

        if start_string == end_string:
            return f"{array_string}[{start_string}]"

        return f"{array_string}[{start_string}:{end_string}]"


    def lphy_string(self):
        array_string = self.array.lphy_string() if not self.array.is_anonymous() else self.array.get_id()
        start_string = self.start.lphy_string()
        end_string = self.end.lphy_string()

        if not self.start.is_anonymous() or not self.end.is_anonymous():
            return super().lphy_string()

        if start_string == end_string:
            return f"{array_string}[{start_string}]"

        return f"{array_string}[{start_string}:{end_string}]"

    # def size(self):
    #     return self.end - self.start + 1
