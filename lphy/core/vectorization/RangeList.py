from abc import ABC

from lphy.core.model.Function import Function
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.model.Value import Value


class RangeList(Function, ABC):
    range_elements = []

    def __init__(self, *range_elements):
        arg = 0
        for node in range_elements:
            value = node.value()
            if isinstance(value, (int, list)):
                self.range_elements.append(node)
                if isinstance(node, Value):
                    self.set_input(node)
                elif isinstance(node, Function):
                    self.set_input(node.apply())
                arg += 1
            else:
                ValueError(f"Non integer in RangeList: {value}")

    #TODO def apply(self) -> IntegerArrayValue:
    #     indices = []
    #     for node in self.range_elements:
    #         value = node.value()
    #         if isinstance(value, int):
    #             indices.append(value)
    #         else:
    #             indices.extend(value)
    #     return IntegerArrayValue(None, indices, self)
    #
    # def is_range(self) -> bool:
    #     return len(self.range_elements) == 1 and isinstance(self.range_elements[0], Range)

    def is_single(self) -> bool:
        return len(self.range_elements) == 1 and isinstance(self.range_elements[0].value(), int)

    def get_range_element(self, i: int) -> GraphicalModelNode:
        return self.range_elements[i]

    def size(self) -> int:
        return len(self.range_elements)

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
