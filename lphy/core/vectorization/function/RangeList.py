from abc import ABC
from typing import List

from lphy.core.model.Function import Function, DeterministicFunction
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.model.Value import Value


def is_all_int(value):
    return isinstance(value, int) or all(isinstance(elem, int) for elem in value)


class RangeList(DeterministicFunction, ABC):
    """
    The element can be Value or Function
    """
    range_elements: List[Value] = []

    def __init__(self, element_list):
        super().__init__()
        arg = 0
        for node in element_list:
            if isinstance(node, Value) and is_all_int(node.value):
                #TODO set_input("arg_" + arg, node)
                self.set_input(node)
            elif isinstance(node, DeterministicFunction): # apply() may produce Value(None)
                # TODO set_input("arg_" + arg, node)
                self.set_input(node.apply())
            else:
                ValueError(f"Non integer in RangeList: {node}")
            self.range_elements.append(node)
            arg += 1

    def apply(self) -> Value:
        indices = []
        for node in self.range_elements:
            value = node.value
            if isinstance(value, int):
                indices.append(value)
            else:
                indices.extend(value)
        return Value(None, indices, self)

    # def is_range(self) -> bool:
    #     return len(self.range_elements) == 1 and isinstance(self.range_elements[0], Range)

    # def is_single(self) -> bool:
    #     return len(self.range_elements) == 1 and isinstance(self.range_elements[0].value, int)

    def get_range_element(self, i: int) -> Value:
        return self.range_elements[i]

    def size(self) -> int:
        return len(self.range_elements)

    def lphy_to_rev(self, var_name) -> str:
        return self.lphy_string()

    def lphy_string(self) -> str:
        builder = []
        for node in self.range_elements:
            if builder:
                builder.append(",")
            if isinstance(node, Value):
                if node.is_anonymous():
                    builder.append(node.lphy_string())
                else:
                    builder.append(node.get_id())
            elif isinstance(node, Function):
                builder.append(node.lphy_string())
        return ",".join(builder)



#TODO replaced by python range
# class Range(DeterministicFunction, ABC):
#     # if attr generator_info defines the function name, then use it, otherwise use class name
#     generator_info = {"name": "rangeInt",
#                       "description": "The range of integers from start to end. Boundaries are included."}
#
#     def __init__(self, start: Value, end: Value):
#         super().__init__()
#         # start of the range (inclusive)
#         self.start = start
#         # end of the range (inclusive)
#         self.end = end
#
#     def apply(self) -> "Value":
#         s = self.start.value
#         e = self.end.value
#         return Value(None, range(s, e+1), self)
#
#     def lphy_to_rev(self, var_name):
#         return f"{self.start.lphy_to_rev(var_name)}:{self.end.lphy_to_rev(var_name)}"
#
#     def lphy_string(self):
#         from lphy.core.error.Errors import UnsupportedOperationException
#         raise UnsupportedOperationException("TODO")
