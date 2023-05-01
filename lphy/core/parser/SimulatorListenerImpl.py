from core.parser.SimulatorBaseListener import SimulatorBaseListener
from core.parser.SimulatorParser import *

import LPhyParserAction


class SimulatorListenerImpl(SimulatorBaseListener, LPhyParserAction):

    DATA = 0
    MODEL = 1

    def __init__(self, parser, context):
        self.parser = parser
        self.context = context

    def put(self, strId: str, value):
        if self.context == self.DATA:
            self.parser.getDataDictionary().put(strId, value)
            self.parser.getDataValues().add(value)
        elif self.context == self.MODEL:
            pass
        else:
            self.parser.getModelDictionary().put(strId, value)
            self.parser.getModelValues().add(value)

    def get(self, strId: str):
        return self.parser.getValue(strId, self.context)

    def containsKey(self, strId: str):
        return self.parser.hasValue(strId, self.context)


class SimulatorASTVisitor(SimulatorBaseListener):

    def visitRange_list(self, ctx: SimulatorParser.Range_listContext):
        nodes = []

        for i in range(ctx.getChildCount()):
            o = super(SimulatorBaseListener, self).visit(ctx.getChild(i))

