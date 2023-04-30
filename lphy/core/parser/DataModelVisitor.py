# Generated from LPhyRevPy/lphy/core/parser/DataModel.g4 by ANTLR 4.12.0

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DataModelParser import DataModelParser
else:
    from DataModelParser import DataModelParser

# This class defines a complete generic visitor for a parse tree produced by DataModelParser.

class DataModelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DataModelParser#input.
    def visitInput(self, ctx:DataModelParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#datablock.
    def visitDatablock(self, ctx:DataModelParser.DatablockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#modelblock.
    def visitModelblock(self, ctx:DataModelParser.ModelblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#relations.
    def visitRelations(self, ctx:DataModelParser.RelationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#determ_relations.
    def visitDeterm_relations(self, ctx:DataModelParser.Determ_relationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#relation_list.
    def visitRelation_list(self, ctx:DataModelParser.Relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#determ_relation_list.
    def visitDeterm_relation_list(self, ctx:DataModelParser.Determ_relation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#determ_relation_line.
    def visitDeterm_relation_line(self, ctx:DataModelParser.Determ_relation_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#relation.
    def visitRelation(self, ctx:DataModelParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#for_loop.
    def visitFor_loop(self, ctx:DataModelParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#counter.
    def visitCounter(self, ctx:DataModelParser.CounterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#assignment.
    def visitAssignment(self, ctx:DataModelParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#determ_relation.
    def visitDeterm_relation(self, ctx:DataModelParser.Determ_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#stoch_relation.
    def visitStoch_relation(self, ctx:DataModelParser.Stoch_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#var.
    def visitVar(self, ctx:DataModelParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#range_list.
    def visitRange_list(self, ctx:DataModelParser.Range_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#range_element.
    def visitRange_element(self, ctx:DataModelParser.Range_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#constant.
    def visitConstant(self, ctx:DataModelParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#expression_list.
    def visitExpression_list(self, ctx:DataModelParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#unnamed_expression_list.
    def visitUnnamed_expression_list(self, ctx:DataModelParser.Unnamed_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#mapFunction.
    def visitMapFunction(self, ctx:DataModelParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#methodCall.
    def visitMethodCall(self, ctx:DataModelParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#objectMethodCall.
    def visitObjectMethodCall(self, ctx:DataModelParser.ObjectMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#distribution.
    def visitDistribution(self, ctx:DataModelParser.DistributionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#named_expression.
    def visitNamed_expression(self, ctx:DataModelParser.Named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataModelParser#expression.
    def visitExpression(self, ctx:DataModelParser.ExpressionContext):
        return self.visitChildren(ctx)



del DataModelParser