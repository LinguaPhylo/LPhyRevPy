

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

    def getValue(self, __id, context):
        match context:
            case "data":
                return self.getDataDictionary().get(__id)
            case "model" | _:
                _data = self.getDataDictionary()
                _model = self.getModelDictionary()
                if __id in _model:
                    return _model.get(__id)
                return _data.get(__id)

    def hasValue(self, __id, context):
        return bool(self.getValue(__id, context))

