from lphy.core.error.Errors import ParsingException
from lphy.core.graphicalmodel.Function import Function
from lphy.core.parser.antlr.LPhyParser import LPhyParser
from lphy.core.parser.antlr.LPhyVisitor import LPhyVisitor
from lphy.core.vectorization.RangeList import RangeList


class LPhyASTVisitor(LPhyVisitor):

    # Override methods as needed for AST-specific operations
    # def visitInput(self, ctx:LPhyParser.InputContext):
    #     # Your AST-specific visitInput implementation here
    #     return super().visitChildren(ctx)

    def visitStructured_input(self, ctx: LPhyParser.Structured_inputContext):
        return super().visitStructured_input(ctx)

    def visitFree_lines(self, ctx: LPhyParser.Free_linesContext):
        return super().visitFree_lines(ctx)

    def visitDatablock(self, ctx: LPhyParser.DatablockContext):
        return super().visitDatablock(ctx)

    def visitDeterm_relation_list(self, ctx: LPhyParser.Determ_relation_listContext):
        return super().visitDeterm_relation_list(ctx)

    def visitDeterm_relation_line(self, ctx: LPhyParser.Determ_relation_lineContext):
        return super().visitDeterm_relation_line(ctx)

    def visitModelblock(self, ctx: LPhyParser.ModelblockContext):
        return super().visitModelblock(ctx)

    def visitRelation_list(self, ctx: LPhyParser.Relation_listContext):
        return super().visitRelation_list(ctx)

    def visitRelation(self, ctx: LPhyParser.RelationContext):
        return super().visitRelation(ctx)

    def visitVar(self, ctx: LPhyParser.VarContext):
        return super().visitVar(ctx)

    # return a RangeList function.
    def visitRange_list(self, ctx: LPhyParser.Range_listContext):
        return self.visitChildren(ctx)
        #TODO
        nodes = []

        for i in range(ctx.getChildCount()):
            o = self.visit(ctx.getChild(i))

            if isinstance(o, (IntegerValue, IntegerArrayValue, Range)):
                nodes.append(o)
            elif isinstance(o, Function):
                f = o
                if isinstance(f.value(), (int, list)):
                    nodes.append(o)
                else:
                    error_message = "Expected function returning Integer or Integer[]: " + str(o)
                    raise ParsingException(error_message, ctx)
            elif o is None:
                # ignore commas
                pass
            else:
                error_message = "Expected Integer value, or Range, in range list, but found: " + str(o)
                raise ParsingException(error_message, ctx)

        return RangeList(nodes)

    def visitDeterm_relation(self, ctx: LPhyParser.Determ_relationContext):
        return super().visitDeterm_relation(ctx)

    def visitStoch_relation(self, ctx: LPhyParser.Stoch_relationContext):
        # TODO
        return super().visitStoch_relation(ctx)

    def visitLiteral(self, ctx: LPhyParser.LiteralContext):
        return super().visitLiteral(ctx)

    def visitFloatingPointLiteral(self, ctx: LPhyParser.FloatingPointLiteralContext):
        return super().visitFloatingPointLiteral(ctx)

    def visitIntegerLiteral(self, ctx: LPhyParser.IntegerLiteralContext):
        return super().visitIntegerLiteral(ctx)

    def visitBooleanLiteral(self, ctx: LPhyParser.BooleanLiteralContext):
        return super().visitBooleanLiteral(ctx)

    def visitExpression_list(self, ctx: LPhyParser.Expression_listContext):
        # TODO
        return super().visitExpression_list(ctx)

    def visitUnnamed_expression_list(self, ctx: LPhyParser.Unnamed_expression_listContext):
        # TODO
        return super().visitUnnamed_expression_list(ctx)

    def visitMapFunction(self, ctx: LPhyParser.MapFunctionContext):
        return super().visitMapFunction(ctx)

    def visitFunction(self, ctx: LPhyParser.FunctionContext):
        return super().visitFunction(ctx)

    def visitMethodCall(self, ctx: LPhyParser.MethodCallContext):
        return super().visitMethodCall(ctx)

    def visitDistribution(self, ctx: LPhyParser.DistributionContext):
        return super().visitDistribution(ctx)

    def visitNamed_expression(self, ctx: LPhyParser.Named_expressionContext):
        # TODO
        return super().visitNamed_expression(ctx)

    def visitArray_construction(self, ctx: LPhyParser.Array_constructionContext):
        return super().visitArray_construction(ctx)

    def visitExpression(self, ctx: LPhyParser.ExpressionContext):
        # TODO
        return super().visitExpression(ctx)


