# Generated from ~/WorkSpace/LPhyRevPy/lphy/core/parser/DataModel.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DataModelParser import DataModelParser
else:
    from DataModelParser import DataModelParser

# This class defines a complete listener for a parse tree produced by DataModelParser.
class DataModelListener(ParseTreeListener):

    # Enter a parse tree produced by DataModelParser#input.
    def enterInput(self, ctx:DataModelParser.InputContext):
        pass

    # Exit a parse tree produced by DataModelParser#input.
    def exitInput(self, ctx:DataModelParser.InputContext):
        pass


    # Enter a parse tree produced by DataModelParser#datablock.
    def enterDatablock(self, ctx:DataModelParser.DatablockContext):
        pass

    # Exit a parse tree produced by DataModelParser#datablock.
    def exitDatablock(self, ctx:DataModelParser.DatablockContext):
        pass


    # Enter a parse tree produced by DataModelParser#modelblock.
    def enterModelblock(self, ctx:DataModelParser.ModelblockContext):
        pass

    # Exit a parse tree produced by DataModelParser#modelblock.
    def exitModelblock(self, ctx:DataModelParser.ModelblockContext):
        pass


    # Enter a parse tree produced by DataModelParser#relations.
    def enterRelations(self, ctx:DataModelParser.RelationsContext):
        pass

    # Exit a parse tree produced by DataModelParser#relations.
    def exitRelations(self, ctx:DataModelParser.RelationsContext):
        pass


    # Enter a parse tree produced by DataModelParser#determ_relations.
    def enterDeterm_relations(self, ctx:DataModelParser.Determ_relationsContext):
        pass

    # Exit a parse tree produced by DataModelParser#determ_relations.
    def exitDeterm_relations(self, ctx:DataModelParser.Determ_relationsContext):
        pass


    # Enter a parse tree produced by DataModelParser#relation_list.
    def enterRelation_list(self, ctx:DataModelParser.Relation_listContext):
        pass

    # Exit a parse tree produced by DataModelParser#relation_list.
    def exitRelation_list(self, ctx:DataModelParser.Relation_listContext):
        pass


    # Enter a parse tree produced by DataModelParser#determ_relation_list.
    def enterDeterm_relation_list(self, ctx:DataModelParser.Determ_relation_listContext):
        pass

    # Exit a parse tree produced by DataModelParser#determ_relation_list.
    def exitDeterm_relation_list(self, ctx:DataModelParser.Determ_relation_listContext):
        pass


    # Enter a parse tree produced by DataModelParser#determ_relation_line.
    def enterDeterm_relation_line(self, ctx:DataModelParser.Determ_relation_lineContext):
        pass

    # Exit a parse tree produced by DataModelParser#determ_relation_line.
    def exitDeterm_relation_line(self, ctx:DataModelParser.Determ_relation_lineContext):
        pass


    # Enter a parse tree produced by DataModelParser#relation.
    def enterRelation(self, ctx:DataModelParser.RelationContext):
        pass

    # Exit a parse tree produced by DataModelParser#relation.
    def exitRelation(self, ctx:DataModelParser.RelationContext):
        pass


    # Enter a parse tree produced by DataModelParser#for_loop.
    def enterFor_loop(self, ctx:DataModelParser.For_loopContext):
        pass

    # Exit a parse tree produced by DataModelParser#for_loop.
    def exitFor_loop(self, ctx:DataModelParser.For_loopContext):
        pass


    # Enter a parse tree produced by DataModelParser#counter.
    def enterCounter(self, ctx:DataModelParser.CounterContext):
        pass

    # Exit a parse tree produced by DataModelParser#counter.
    def exitCounter(self, ctx:DataModelParser.CounterContext):
        pass


    # Enter a parse tree produced by DataModelParser#assignment.
    def enterAssignment(self, ctx:DataModelParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DataModelParser#assignment.
    def exitAssignment(self, ctx:DataModelParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DataModelParser#determ_relation.
    def enterDeterm_relation(self, ctx:DataModelParser.Determ_relationContext):
        pass

    # Exit a parse tree produced by DataModelParser#determ_relation.
    def exitDeterm_relation(self, ctx:DataModelParser.Determ_relationContext):
        pass


    # Enter a parse tree produced by DataModelParser#stoch_relation.
    def enterStoch_relation(self, ctx:DataModelParser.Stoch_relationContext):
        pass

    # Exit a parse tree produced by DataModelParser#stoch_relation.
    def exitStoch_relation(self, ctx:DataModelParser.Stoch_relationContext):
        pass


    # Enter a parse tree produced by DataModelParser#var.
    def enterVar(self, ctx:DataModelParser.VarContext):
        pass

    # Exit a parse tree produced by DataModelParser#var.
    def exitVar(self, ctx:DataModelParser.VarContext):
        pass


    # Enter a parse tree produced by DataModelParser#range_list.
    def enterRange_list(self, ctx:DataModelParser.Range_listContext):
        pass

    # Exit a parse tree produced by DataModelParser#range_list.
    def exitRange_list(self, ctx:DataModelParser.Range_listContext):
        pass


    # Enter a parse tree produced by DataModelParser#range_element.
    def enterRange_element(self, ctx:DataModelParser.Range_elementContext):
        pass

    # Exit a parse tree produced by DataModelParser#range_element.
    def exitRange_element(self, ctx:DataModelParser.Range_elementContext):
        pass


    # Enter a parse tree produced by DataModelParser#constant.
    def enterConstant(self, ctx:DataModelParser.ConstantContext):
        pass

    # Exit a parse tree produced by DataModelParser#constant.
    def exitConstant(self, ctx:DataModelParser.ConstantContext):
        pass


    # Enter a parse tree produced by DataModelParser#expression_list.
    def enterExpression_list(self, ctx:DataModelParser.Expression_listContext):
        pass

    # Exit a parse tree produced by DataModelParser#expression_list.
    def exitExpression_list(self, ctx:DataModelParser.Expression_listContext):
        pass


    # Enter a parse tree produced by DataModelParser#unnamed_expression_list.
    def enterUnnamed_expression_list(self, ctx:DataModelParser.Unnamed_expression_listContext):
        pass

    # Exit a parse tree produced by DataModelParser#unnamed_expression_list.
    def exitUnnamed_expression_list(self, ctx:DataModelParser.Unnamed_expression_listContext):
        pass


    # Enter a parse tree produced by DataModelParser#mapFunction.
    def enterMapFunction(self, ctx:DataModelParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by DataModelParser#mapFunction.
    def exitMapFunction(self, ctx:DataModelParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by DataModelParser#methodCall.
    def enterMethodCall(self, ctx:DataModelParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DataModelParser#methodCall.
    def exitMethodCall(self, ctx:DataModelParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DataModelParser#objectMethodCall.
    def enterObjectMethodCall(self, ctx:DataModelParser.ObjectMethodCallContext):
        pass

    # Exit a parse tree produced by DataModelParser#objectMethodCall.
    def exitObjectMethodCall(self, ctx:DataModelParser.ObjectMethodCallContext):
        pass


    # Enter a parse tree produced by DataModelParser#distribution.
    def enterDistribution(self, ctx:DataModelParser.DistributionContext):
        pass

    # Exit a parse tree produced by DataModelParser#distribution.
    def exitDistribution(self, ctx:DataModelParser.DistributionContext):
        pass


    # Enter a parse tree produced by DataModelParser#named_expression.
    def enterNamed_expression(self, ctx:DataModelParser.Named_expressionContext):
        pass

    # Exit a parse tree produced by DataModelParser#named_expression.
    def exitNamed_expression(self, ctx:DataModelParser.Named_expressionContext):
        pass


    # Enter a parse tree produced by DataModelParser#expression.
    def enterExpression(self, ctx:DataModelParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DataModelParser#expression.
    def exitExpression(self, ctx:DataModelParser.ExpressionContext):
        pass



del DataModelParser