from LPhyMetaParser import LPhyMetaParser
from lphy.core.error.Errors import ParsingException
from lphy.core.graphicalmodel.Function import Function
from antlr.LPhyParser import LPhyParser
from antlr.LPhyVisitor import LPhyVisitor
from lphy.core.vectorization.RangeList import RangeList


class LPhyASTVisitor(LPhyVisitor):

    def __init__(self, meta_parser: LPhyMetaParser, context: str):
        self._context = context
        self._meta_parser = meta_parser

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
        # TODO
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
        if self._context == LPhyMetaParser.DATA:
            raise ParsingException("Generative distributions are not allowed in the data block! "
                                   "Use model block for Generative distributions.", ctx)

        gen_dist = self.visit(ctx.getChild(2))
        var = self.visit(ctx.getChild(0))
        variable = gen_dist.create_var_by_id(var.get_id())

        # TODO
        # if isinstance(gen_dist, VectorizedDistribution) and DataClampingUtils.is_data_clamping(var, parser):
        #     array = self._meta_parser.data_dict[var.get_id()].value()
        #     if isinstance(array, list):
        #         variable = DataClampingUtils.get_data_clamped_vectorized_random_variable(var.get_id(), gen_dist, array)
        #         print( "Data clamping: the value of " + var.get_id() +
        #                " in the 'model' block is replaced by the value of " +
        #                var.get_id() + " in the 'data' block ." )
        #
        # else:
        #     variable = gen_dist.sample(var.get_id())

        if variable is not None and not var.is_ranged_var():
            self._meta_parser.put(variable.get_id(), variable, self._context)
            return variable
        else:
            raise ParsingException("Data clamping requires to data as array object !", ctx)

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


