

class GraphicalModel:

    # inputs are the arguments of a function or distribution or
    # the function/distribution that produced this model node value/variable.
    def getInputs(self) -> list:
        pass

    # return a unique string representing this graphical model node.
    # For named variables it should be the name.
    def getUniqueId(self) -> str:
        pass
