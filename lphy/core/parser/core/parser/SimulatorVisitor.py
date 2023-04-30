# Generated from ~/WorkSpace/LPhyRevPy/lphy/core/parser/Simulator.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimulatorParser import SimulatorParser
else:
    from SimulatorParser import SimulatorParser

# This class defines a complete generic visitor for a parse tree produced by SimulatorParser.

class SimulatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimulatorParser#input.
    def visitInput(self, ctx:SimulatorParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#relations.
    def visitRelations(self, ctx:SimulatorParser.RelationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#relation_list.
    def visitRelation_list(self, ctx:SimulatorParser.Relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#relation.
    def visitRelation(self, ctx:SimulatorParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#assignment.
    def visitAssignment(self, ctx:SimulatorParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#determ_relation.
    def visitDeterm_relation(self, ctx:SimulatorParser.Determ_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#stoch_relation.
    def visitStoch_relation(self, ctx:SimulatorParser.Stoch_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#var.
    def visitVar(self, ctx:SimulatorParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#range_list.
    def visitRange_list(self, ctx:SimulatorParser.Range_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#range_element.
    def visitRange_element(self, ctx:SimulatorParser.Range_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#constant.
    def visitConstant(self, ctx:SimulatorParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#expression_list.
    def visitExpression_list(self, ctx:SimulatorParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#unnamed_expression_list.
    def visitUnnamed_expression_list(self, ctx:SimulatorParser.Unnamed_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#mapFunction.
    def visitMapFunction(self, ctx:SimulatorParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#methodCall.
    def visitMethodCall(self, ctx:SimulatorParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#objectMethodCall.
    def visitObjectMethodCall(self, ctx:SimulatorParser.ObjectMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#distribution.
    def visitDistribution(self, ctx:SimulatorParser.DistributionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#named_expression.
    def visitNamed_expression(self, ctx:SimulatorParser.Named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimulatorParser#expression.
    def visitExpression(self, ctx:SimulatorParser.ExpressionContext):
        return self.visitChildren(ctx)



del SimulatorParser