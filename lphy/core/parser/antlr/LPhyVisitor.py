# Generated from lphy/core/parser/antlr/LPhy.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LPhyParser import LPhyParser
else:
    from LPhyParser import LPhyParser

# This class defines a complete generic visitor for a parse tree produced by LPhyParser.

class LPhyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPhyParser#input.
    def visitInput(self, ctx:LPhyParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#structured_input.
    def visitStructured_input(self, ctx:LPhyParser.Structured_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#free_lines.
    def visitFree_lines(self, ctx:LPhyParser.Free_linesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#datablock.
    def visitDatablock(self, ctx:LPhyParser.DatablockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#determ_relation_list.
    def visitDeterm_relation_list(self, ctx:LPhyParser.Determ_relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#determ_relation_line.
    def visitDeterm_relation_line(self, ctx:LPhyParser.Determ_relation_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#modelblock.
    def visitModelblock(self, ctx:LPhyParser.ModelblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#relation_list.
    def visitRelation_list(self, ctx:LPhyParser.Relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#relation.
    def visitRelation(self, ctx:LPhyParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#var.
    def visitVar(self, ctx:LPhyParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#range_list.
    def visitRange_list(self, ctx:LPhyParser.Range_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#determ_relation.
    def visitDeterm_relation(self, ctx:LPhyParser.Determ_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#stoch_relation.
    def visitStoch_relation(self, ctx:LPhyParser.Stoch_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#literal.
    def visitLiteral(self, ctx:LPhyParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#floatingPointLiteral.
    def visitFloatingPointLiteral(self, ctx:LPhyParser.FloatingPointLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:LPhyParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:LPhyParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#expression_list.
    def visitExpression_list(self, ctx:LPhyParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#unnamed_expression_list.
    def visitUnnamed_expression_list(self, ctx:LPhyParser.Unnamed_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#mapFunction.
    def visitMapFunction(self, ctx:LPhyParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#function.
    def visitFunction(self, ctx:LPhyParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#methodCall.
    def visitMethodCall(self, ctx:LPhyParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#distribution.
    def visitDistribution(self, ctx:LPhyParser.DistributionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#named_expression.
    def visitNamed_expression(self, ctx:LPhyParser.Named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#array_construction.
    def visitArray_construction(self, ctx:LPhyParser.Array_constructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPhyParser#expression.
    def visitExpression(self, ctx:LPhyParser.ExpressionContext):
        return self.visitChildren(ctx)



del LPhyParser