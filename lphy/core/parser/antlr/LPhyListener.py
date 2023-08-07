# Generated from lphy/core/parser/antlr/LPhy.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LPhyParser import LPhyParser
else:
    from LPhyParser import LPhyParser

# This class defines a complete listener for a parse tree produced by LPhyParser.
class LPhyListener(ParseTreeListener):

    # Enter a parse tree produced by LPhyParser#input.
    def enterInput(self, ctx:LPhyParser.InputContext):
        pass

    # Exit a parse tree produced by LPhyParser#input.
    def exitInput(self, ctx:LPhyParser.InputContext):
        pass


    # Enter a parse tree produced by LPhyParser#structured_input.
    def enterStructured_input(self, ctx:LPhyParser.Structured_inputContext):
        pass

    # Exit a parse tree produced by LPhyParser#structured_input.
    def exitStructured_input(self, ctx:LPhyParser.Structured_inputContext):
        pass


    # Enter a parse tree produced by LPhyParser#free_lines.
    def enterFree_lines(self, ctx:LPhyParser.Free_linesContext):
        pass

    # Exit a parse tree produced by LPhyParser#free_lines.
    def exitFree_lines(self, ctx:LPhyParser.Free_linesContext):
        pass


    # Enter a parse tree produced by LPhyParser#datablock.
    def enterDatablock(self, ctx:LPhyParser.DatablockContext):
        pass

    # Exit a parse tree produced by LPhyParser#datablock.
    def exitDatablock(self, ctx:LPhyParser.DatablockContext):
        pass


    # Enter a parse tree produced by LPhyParser#determ_relation_list.
    def enterDeterm_relation_list(self, ctx:LPhyParser.Determ_relation_listContext):
        pass

    # Exit a parse tree produced by LPhyParser#determ_relation_list.
    def exitDeterm_relation_list(self, ctx:LPhyParser.Determ_relation_listContext):
        pass


    # Enter a parse tree produced by LPhyParser#determ_relation_line.
    def enterDeterm_relation_line(self, ctx:LPhyParser.Determ_relation_lineContext):
        pass

    # Exit a parse tree produced by LPhyParser#determ_relation_line.
    def exitDeterm_relation_line(self, ctx:LPhyParser.Determ_relation_lineContext):
        pass


    # Enter a parse tree produced by LPhyParser#modelblock.
    def enterModelblock(self, ctx:LPhyParser.ModelblockContext):
        pass

    # Exit a parse tree produced by LPhyParser#modelblock.
    def exitModelblock(self, ctx:LPhyParser.ModelblockContext):
        pass


    # Enter a parse tree produced by LPhyParser#relation_list.
    def enterRelation_list(self, ctx:LPhyParser.Relation_listContext):
        pass

    # Exit a parse tree produced by LPhyParser#relation_list.
    def exitRelation_list(self, ctx:LPhyParser.Relation_listContext):
        pass


    # Enter a parse tree produced by LPhyParser#relation.
    def enterRelation(self, ctx:LPhyParser.RelationContext):
        pass

    # Exit a parse tree produced by LPhyParser#relation.
    def exitRelation(self, ctx:LPhyParser.RelationContext):
        pass


    # Enter a parse tree produced by LPhyParser#var.
    def enterVar(self, ctx:LPhyParser.VarContext):
        pass

    # Exit a parse tree produced by LPhyParser#var.
    def exitVar(self, ctx:LPhyParser.VarContext):
        pass


    # Enter a parse tree produced by LPhyParser#range_list.
    def enterRange_list(self, ctx:LPhyParser.Range_listContext):
        pass

    # Exit a parse tree produced by LPhyParser#range_list.
    def exitRange_list(self, ctx:LPhyParser.Range_listContext):
        pass


    # Enter a parse tree produced by LPhyParser#determ_relation.
    def enterDeterm_relation(self, ctx:LPhyParser.Determ_relationContext):
        pass

    # Exit a parse tree produced by LPhyParser#determ_relation.
    def exitDeterm_relation(self, ctx:LPhyParser.Determ_relationContext):
        pass


    # Enter a parse tree produced by LPhyParser#stoch_relation.
    def enterStoch_relation(self, ctx:LPhyParser.Stoch_relationContext):
        pass

    # Exit a parse tree produced by LPhyParser#stoch_relation.
    def exitStoch_relation(self, ctx:LPhyParser.Stoch_relationContext):
        pass


    # Enter a parse tree produced by LPhyParser#literal.
    def enterLiteral(self, ctx:LPhyParser.LiteralContext):
        pass

    # Exit a parse tree produced by LPhyParser#literal.
    def exitLiteral(self, ctx:LPhyParser.LiteralContext):
        pass


    # Enter a parse tree produced by LPhyParser#floatingPointLiteral.
    def enterFloatingPointLiteral(self, ctx:LPhyParser.FloatingPointLiteralContext):
        pass

    # Exit a parse tree produced by LPhyParser#floatingPointLiteral.
    def exitFloatingPointLiteral(self, ctx:LPhyParser.FloatingPointLiteralContext):
        pass


    # Enter a parse tree produced by LPhyParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:LPhyParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by LPhyParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:LPhyParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by LPhyParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:LPhyParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by LPhyParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:LPhyParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by LPhyParser#expression_list.
    def enterExpression_list(self, ctx:LPhyParser.Expression_listContext):
        pass

    # Exit a parse tree produced by LPhyParser#expression_list.
    def exitExpression_list(self, ctx:LPhyParser.Expression_listContext):
        pass


    # Enter a parse tree produced by LPhyParser#unnamed_expression_list.
    def enterUnnamed_expression_list(self, ctx:LPhyParser.Unnamed_expression_listContext):
        pass

    # Exit a parse tree produced by LPhyParser#unnamed_expression_list.
    def exitUnnamed_expression_list(self, ctx:LPhyParser.Unnamed_expression_listContext):
        pass


    # Enter a parse tree produced by LPhyParser#mapFunction.
    def enterMapFunction(self, ctx:LPhyParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by LPhyParser#mapFunction.
    def exitMapFunction(self, ctx:LPhyParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by LPhyParser#function.
    def enterFunction(self, ctx:LPhyParser.FunctionContext):
        pass

    # Exit a parse tree produced by LPhyParser#function.
    def exitFunction(self, ctx:LPhyParser.FunctionContext):
        pass


    # Enter a parse tree produced by LPhyParser#methodCall.
    def enterMethodCall(self, ctx:LPhyParser.MethodCallContext):
        pass

    # Exit a parse tree produced by LPhyParser#methodCall.
    def exitMethodCall(self, ctx:LPhyParser.MethodCallContext):
        pass


    # Enter a parse tree produced by LPhyParser#distribution.
    def enterDistribution(self, ctx:LPhyParser.DistributionContext):
        pass

    # Exit a parse tree produced by LPhyParser#distribution.
    def exitDistribution(self, ctx:LPhyParser.DistributionContext):
        pass


    # Enter a parse tree produced by LPhyParser#named_expression.
    def enterNamed_expression(self, ctx:LPhyParser.Named_expressionContext):
        pass

    # Exit a parse tree produced by LPhyParser#named_expression.
    def exitNamed_expression(self, ctx:LPhyParser.Named_expressionContext):
        pass


    # Enter a parse tree produced by LPhyParser#array_construction.
    def enterArray_construction(self, ctx:LPhyParser.Array_constructionContext):
        pass

    # Exit a parse tree produced by LPhyParser#array_construction.
    def exitArray_construction(self, ctx:LPhyParser.Array_constructionContext):
        pass


    # Enter a parse tree produced by LPhyParser#expression.
    def enterExpression(self, ctx:LPhyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LPhyParser#expression.
    def exitExpression(self, ctx:LPhyParser.ExpressionContext):
        pass



del LPhyParser