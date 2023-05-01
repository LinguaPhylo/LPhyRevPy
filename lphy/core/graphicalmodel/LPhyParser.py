from abc import abstractmethod
from typing import overload

from core.graphicalmodel.GraphicalModel import GraphicalModel


class LPhyParser(GraphicalModel):

    @abstractmethod
    def getName(self):
        pass

    def getNamedValuesByType(self, type):
        valuesData = super().getDataDictionary().values()
        valuesDataByType = [v if isinstance(v, type) and not v.isAnonymous() else None for v in valuesData]
        valuesModel = super().getModelDictionary().values()
        valuesModelByType = [v if isinstance(v, type) and not v.isAnonymous() else None for v in valuesModel]
        valuesDataByType.extend(valuesModelByType)
        return [i for i in valuesDataByType if i is not None]

    @abstractmethod
    def getGeneratorClasses(self):
        pass

    @abstractmethod
    def getLines(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    def getKeywords(self):
        keywords = []
        keywords.extend(self.getGeneratorClasses().keys())
        return keywords

    @overload
    def parse(self, code: str):
        self.parse(code, GraphicalModel.context.model)

    @abstractmethod
    def parse(self, code: str, context):
        pass

    def source(self, sourceFile):
        builderStr = ""
        reader = open(sourceFile, "r")
        for line in reader.readlines():
            builderStr + line + "\n"
        reader.close()
        self.parse(builderStr)

    