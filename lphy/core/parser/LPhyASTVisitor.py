import logging
import numpy as np
from typing import List

from lphy.core.parser.antlr.LPhyParser import LPhyParser
from lphy.core.parser.antlr.LPhyVisitor import LPhyVisitor
from lphy.core.error.Errors import ParsingException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.parser import ParserUtils

from lphy.core.parser.argument.ArgumentValue import ArgumentValue
from lphy.core.vectorization.RangeList import RangeList


def _get_value_or_function(obj, ctx, meta_parser: "LPhyMetaParser", block: str):
    if isinstance(obj, Value):
        meta_parser.add_to_value_set(obj, block)
        return obj
    if isinstance(obj, DeterministicFunction):
        func = obj
        val = func.apply()
        val.set_function(func)
        meta_parser.add_to_value_set(val, block)
        return val
    raise ParsingException(f"Expecting value or function but got {obj} !", ctx)


class LPhyASTVisitor(LPhyVisitor):

    # type hint with forward declaration LPhyMetaParser, to avoid circular dependencies
    def __init__(self, meta_parser: "LPhyMetaParser", block: str):
        self._block = block
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
        # TODO
        nodes = []

        for i in range(ctx.getChildCount()):
            o = self.visit(ctx.getChild(i))

            if isinstance(o, (IntegerValue, IntegerArrayValue, Range)):
                nodes.append(o)
            elif isinstance(o, DeterministicFunction):
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
        from .LPhyMetaParser import LPhyMetaParser
        if self._block == LPhyMetaParser.DATA:
            raise ParsingException("Generative distributions are not allowed in the data block! "
                                   "Use model block for Generative distributions.", ctx)

        gen_dist = self.visit(ctx.getChild(2))
        var = self.visit(ctx.getChild(0))

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

        # it only provides id, no value is sampled
        variable = gen_dist.sample(var.get_id())

        if variable is not None and not var.is_ranged_var():
            self._meta_parser.put(variable.get_id(), variable, self._block)
            return variable
        else:
            raise ParsingException("Data clamping requires to data as array object !", ctx)

    def visitLiteral(self, ctx: LPhyParser.LiteralContext):
        text = ctx.getText()
        if text.startswith('"'):
            if text.endswith('"'):
                return Value(text[1:-1])
            else:
                raise RuntimeError(f"Attempted to strip quotes, but the string {text} was not quoted.")
        return Value(text)  # suppose to be constants

    def visitFloatingPointLiteral(self, ctx: LPhyParser.FloatingPointLiteralContext):
        return super().visitFloatingPointLiteral(ctx)

    def visitIntegerLiteral(self, ctx: LPhyParser.IntegerLiteralContext):
        return super().visitIntegerLiteral(ctx)

    def visitBooleanLiteral(self, ctx: LPhyParser.BooleanLiteralContext):
        return super().visitBooleanLiteral(ctx)

    def visitExpression_list(self, ctx: LPhyParser.Expression_listContext) -> List[ArgumentValue]:
        list_values = [self.visit(ctx.getChild(i)) for i in range(0, ctx.getChildCount(), 2)]
        return list_values

    def visitUnnamed_expression_list(self, ctx: LPhyParser.Unnamed_expression_listContext):
        values = []
        for i in range(0, ctx.getChildCount(), 2):
            obj = self.visit(ctx.getChild(i))
            if isinstance(obj, DeterministicFunction):
                value = obj.apply()
                value.set_function(obj)
                values.append(value)
            elif isinstance(obj, Value):
                value = obj
                values.append(value)
            elif obj is None:
                values.append(None)
            else:
                raise ParsingException("Found a non-value, non-function in unnamed expression list: " + str(obj), ctx)
        return values

    def visitMapFunction(self, ctx: LPhyParser.MapFunctionContext):
        return super().visitMapFunction(ctx)

    def visitFunction(self, ctx: LPhyParser.FunctionContext):
        return super().visitFunction(ctx)

    def visitMethodCall(self, ctx: LPhyParser.MethodCallContext):
        return super().visitMethodCall(ctx)

    def visitDistribution(self, ctx: LPhyParser.DistributionContext):
        name = ctx.getChild(0).getText()
        f = self.visit(ctx.getChild(2))
        arguments = {}

        for v in f:
            if v is not None:
                if isinstance(v, ArgumentValue):
                    arguments[v.get_name()] = v.get_value()
                else:
                    raise ParsingException("Expecting ArgumentValue for " + name + ": " + f, ctx)
            else:
                raise ParsingException("Argument unexpectedly null", ctx)

        # TODO
        matches = ParserUtils.get_matching_generative_distributions(name, arguments)

        if len(matches) == 0:
            raise ParsingException("No generative distribution named " + name +
                                   " found matching arguments " + str(arguments), ctx)
        elif len(matches) == 1:
            generator = matches[0]
            for key, value in arguments.items():
                generator.set_input(key, value)
            return generator
        else:
            logging.warning("Found " + str(len(matches)) + " matches for " + name + ". Picking first one!")
            generator = matches[0]
            for key, value in arguments.items():
                generator.set_input(key, value)
            return generator

    def visitNamed_expression(self, ctx: LPhyParser.Named_expressionContext):
        name = ctx.getChild(0).getText()
        obj = self.visit(ctx.getChild(2))

        if isinstance(obj, DeterministicFunction):
            value = obj.apply()
            value.set_function(obj)
            v = ArgumentValue(name, value, self._meta_parser, self._block)
            return v

        if isinstance(obj, Value):
            value = obj
            v = ArgumentValue(name, value, self._meta_parser, self._block)
            return v

        return obj

    def visitArray_construction(self, ctx: LPhyParser.Array_constructionContext):
        return super().visitArray_construction(ctx)

    # return and array of ArgumentValue objects
    def visitExpression(self, ctx: LPhyParser.ExpressionContext):
        # Deals with single token expressions -- either an id or a map expression
        if ctx.getChildCount() == 1:
            child_context = ctx.getChild(0)
            # if this is a map just return the map Value
            if child_context.getText().startswith("{"):
                obj = self.visit(child_context)
                return obj

            key = child_context.getText()
            if self._meta_parser.has_value(key, self._block):
                return self._meta_parser.get_value(key, self._block)

        expression = None
        if ctx.getChildCount() >= 2:
            s = ctx.getChild(1).getText()
            # getChild(1) to parse the array index, e.g. x[0]
            if s == "[":
                return self._visit_index_range(ctx)

            # TODO: handle built-in functions

            s = ctx.getChild(0).getText()

            if s == "!":
                f1 = self.visit(ctx.getChild(2))
                # TODO expression = ExpressionNode1Arg(ctx.getText(), ExpressionNode1Arg.not_op(), f1)
                return expression
            # Parsing array moves to visit_array_expression

        return super().visitExpression(ctx)

    def _visit_index_range(self, ctx):
        child = self.visit(ctx.getChild(0))

        array = _get_value_or_function(child, ctx)

        if not isinstance(array.value(), (np.ndarray, list)):
            raise ParsingException(f"Expected value {array} to be an array.", ctx)

        range_list = self.visit(ctx.getChild(2))
        # TODO
        return self.get_indexed_value(array, range_list)
