class GraphicalModelNode:

    def __init__(self, value=None):
        self.value = value

    def lphy_to_rev(self):
        pass

    # inputs are the arguments of a function or distribution or
    # the function/distribution that produced this model node value/variable.
    def get_inputs(self):
        pass

    # return a unique string representing this graphical model node.
    # For named variables it should be the name.
    def get_unique_id(self) -> str:
        return str(hash(self))
