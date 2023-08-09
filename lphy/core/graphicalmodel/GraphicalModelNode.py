

class GraphicalModelNode:

    def __init__(self, value):
        self.value = value

    # inputs are the arguments of a function or distribution or
    # the function/distribution that produced this model node value/variable.
    def get_inputs(self):
        return self.get_params().values()

    # return a unique string representing this graphical model node.
    # For named variables it should be the name.
    def get_unique_id(self) -> str:
        pass
