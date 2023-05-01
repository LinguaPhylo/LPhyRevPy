# Generated from LPhyRevPy/lphy/core/parser/Simulator.g4 by ANTLR 4.12.0

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimulatorParser import SimulatorParser
else:
    from SimulatorParser import SimulatorParser


# This class defines a complete listener for a parse tree produced by SimulatorParser.
class SimulatorBaseListener(ParseTreeListener):

    # Enter a parse tree produced by SimulatorParser#input.
    def enterInput(self, ctx:SimulatorParser.InputContext):
        pass

    # Exit a parse tree produced by SimulatorParser#input.
    def exitInput(self, ctx:SimulatorParser.InputContext):
        pass


    # Enter a parse tree produced by SimulatorParser#relations.
    def enterRelations(self, ctx:SimulatorParser.RelationsContext):
        pass

    # Exit a parse tree produced by SimulatorParser#relations.
    def exitRelations(self, ctx:SimulatorParser.RelationsContext):
        pass


    # Enter a parse tree produced by SimulatorParser#relation_list.
    def enterRelation_list(self, ctx:SimulatorParser.Relation_listContext):
        pass

    # Exit a parse tree produced by SimulatorParser#relation_list.
    def exitRelation_list(self, ctx:SimulatorParser.Relation_listContext):
        pass


    # Enter a parse tree produced by SimulatorParser#relation.
    def enterRelation(self, ctx:SimulatorParser.RelationContext):
        pass

    # Exit a parse tree produced by SimulatorParser#relation.
    def exitRelation(self, ctx:SimulatorParser.RelationContext):
        pass


    # Enter a parse tree produced by SimulatorParser#assignment.
    def enterAssignment(self, ctx:SimulatorParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimulatorParser#assignment.
    def exitAssignment(self, ctx:SimulatorParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimulatorParser#determ_relation.
    def enterDeterm_relation(self, ctx:SimulatorParser.Determ_relationContext):
        pass

    # Exit a parse tree produced by SimulatorParser#determ_relation.
    def exitDeterm_relation(self, ctx:SimulatorParser.Determ_relationContext):
        pass


    # Enter a parse tree produced by SimulatorParser#stoch_relation.
    def enterStoch_relation(self, ctx:SimulatorParser.Stoch_relationContext):
        pass

    # Exit a parse tree produced by SimulatorParser#stoch_relation.
    def exitStoch_relation(self, ctx:SimulatorParser.Stoch_relationContext):
        pass


    # Enter a parse tree produced by SimulatorParser#var.
    def enterVar(self, ctx:SimulatorParser.VarContext):
        pass

    # Exit a parse tree produced by SimulatorParser#var.
    def exitVar(self, ctx:SimulatorParser.VarContext):
        pass


    # Enter a parse tree produced by SimulatorParser#range_list.
    def enterRange_list(self, ctx:SimulatorParser.Range_listContext):
        pass

    # Exit a parse tree produced by SimulatorParser#range_list.
    def exitRange_list(self, ctx:SimulatorParser.Range_listContext):
        pass


    # Enter a parse tree produced by SimulatorParser#range_element.
    def enterRange_element(self, ctx:SimulatorParser.Range_elementContext):
        pass

    # Exit a parse tree produced by SimulatorParser#range_element.
    def exitRange_element(self, ctx:SimulatorParser.Range_elementContext):
        pass


    # Enter a parse tree produced by SimulatorParser#constant.
    def enterConstant(self, ctx:SimulatorParser.ConstantContext):
        pass

    # Exit a parse tree produced by SimulatorParser#constant.
    def exitConstant(self, ctx:SimulatorParser.ConstantContext):
        pass


    # Enter a parse tree produced by SimulatorParser#expression_list.
    def enterExpression_list(self, ctx:SimulatorParser.Expression_listContext):
        pass

    # Exit a parse tree produced by SimulatorParser#expression_list.
    def exitExpression_list(self, ctx:SimulatorParser.Expression_listContext):
        pass


    # Enter a parse tree produced by SimulatorParser#unnamed_expression_list.
    def enterUnnamed_expression_list(self, ctx:SimulatorParser.Unnamed_expression_listContext):
        pass

    # Exit a parse tree produced by SimulatorParser#unnamed_expression_list.
    def exitUnnamed_expression_list(self, ctx:SimulatorParser.Unnamed_expression_listContext):
        pass


    # Enter a parse tree produced by SimulatorParser#mapFunction.
    def enterMapFunction(self, ctx:SimulatorParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by SimulatorParser#mapFunction.
    def exitMapFunction(self, ctx:SimulatorParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by SimulatorParser#methodCall.
    def enterMethodCall(self, ctx:SimulatorParser.MethodCallContext):
        pass

    # Exit a parse tree produced by SimulatorParser#methodCall.
    def exitMethodCall(self, ctx:SimulatorParser.MethodCallContext):
        pass


    # Enter a parse tree produced by SimulatorParser#objectMethodCall.
    def enterObjectMethodCall(self, ctx:SimulatorParser.ObjectMethodCallContext):
        pass

    # Exit a parse tree produced by SimulatorParser#objectMethodCall.
    def exitObjectMethodCall(self, ctx:SimulatorParser.ObjectMethodCallContext):
        pass


    # Enter a parse tree produced by SimulatorParser#distribution.
    def enterDistribution(self, ctx:SimulatorParser.DistributionContext):
        pass

    # Exit a parse tree produced by SimulatorParser#distribution.
    def exitDistribution(self, ctx:SimulatorParser.DistributionContext):
        pass


    # Enter a parse tree produced by SimulatorParser#named_expression.
    def enterNamed_expression(self, ctx:SimulatorParser.Named_expressionContext):
        pass

    # Exit a parse tree produced by SimulatorParser#named_expression.
    def exitNamed_expression(self, ctx:SimulatorParser.Named_expressionContext):
        pass


    # Enter a parse tree produced by SimulatorParser#expression.
    def enterExpression(self, ctx:SimulatorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimulatorParser#expression.
    def exitExpression(self, ctx:SimulatorParser.ExpressionContext):
        pass



del SimulatorParser