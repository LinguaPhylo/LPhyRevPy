

class GraphicalModel:
    # ordered and unchangeable
    context = ("data", "model")

    def getDataDictionary(self) -> dict:
        """the data dictionary of values with id's, keyed by id"""
        pass

    def getModelDictionary(self) -> dict:
        """the model dictionary of values with id's, keyed by id"""
        pass

    def getDataValues(self) -> set:
        pass

    def getModelValues(self) -> set:
        pass