from abc import ABC, abstractmethod


class GraphicalModelNode(ABC):

    def __init__(self, id_: str):
        # single trailing underscore avoids conflicts with keywords or built-in names
        self.id = id_

    def set_id(self, id_: str):
        self.id = id_

    def get_id(self):
        return self.id

    def lphy_to_rev(self):
        pass

    # inputs are the arguments of a function or distribution or
    # the function/distribution that produced this model node value/variable.
    @abstractmethod
    def get_inputs(self):
        pass

    # return a unique string representing this graphical model node.
    # For named variables it should be the name.
    @abstractmethod
    def get_unique_id(self) -> str:
        return str(hash(self))
