import ast
import logging
import numpy as np
from typing import List

from antlr4.tree.Tree import ParseTree

from lphy.core.model.Generator import Generator
from lphy.core.model.MapFunction import MapFunction
from lphy.core.model.MethodCall import MethodCall
from lphy.core.model.RangedVar import Var, get_indexed_value
from lphy.core.parser.antlr.LPhyParser import LPhyParser
from lphy.core.parser.antlr.LPhyVisitor import LPhyVisitor
from lphy.core.error.Errors import ParsingException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.parser import ParserUtils
from lphy.core.parser.argument.ArgumentValue import ArgumentValue
from lphy.core.vectorization.function.RangeList import RangeList

# TODO , "&", "|", "<<", ">>", ">>>"
# Binary operators take two operands
binary_operators = {
    "+", "-", "*", "/", "**", "&&", "||", "<=", "<", ">=", ">", "%", ":", "^", "!=", "=="
}
# TODO
# UnivariateStatistic functions
univar_functions = {
    "abs", "acos", "acosh", "asin", "asinh", "atan", "atanh", "cLogLog", "cbrt", "ceil",
    "cos", "cosh", "exp", "expm1", "floor", "log", "log10", "log1p", "logFact", "logGamma",
    "logit", "phi", "probit", "round", "signum", "sin", "sinh", "sqrt", "step", "tan", "tanh"
}


def _get_value_or_function(obj, ctx, parser_dict: "LPhyParserDictionary", block: str):
    if isinstance(obj, Value):
        parser_dict.add_to_value_set(obj, block)
        return obj
    if isinstance(obj, DeterministicFunction):
        func = obj
        val = func.apply()
        val.set_function(func)
        parser_dict.add_to_value_set(val, block)
        return val
    raise ParsingException(f"Expecting value or function but got {obj} !", ctx.getText())


class LPhyASTVisitor(LPhyVisitor):

    # type hint with forward declaration LPhyParserDictionary, to avoid circular dependencies
    def __init__(self, parser_dict: "LPhyParserDictionary"):
        from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary
        # default to model block, e.g., free lines, update it during parsing
        self._block = LPhyParserDictionary.MODEL
        self._parser_dict = parser_dict

    # Override methods as needed for AST-specific operations
    # def visitInput(self, ctx:LPhyParser.InputContext):
    #     # Your AST-specific visitInput implementation here
    #     return super().visitChildren(ctx)

    # def visitStructured_input(self, ctx: LPhyParser.Structured_inputContext):
    #     return super().visitStructured_input(ctx)

    # def visitFree_lines(self, ctx: LPhyParser.Free_linesContext):
    #     return super().visitFree_lines(ctx)

    def visitDatablock(self, ctx: LPhyParser.DatablockContext):
        # change _block = DATA here
        from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary
        self._block = LPhyParserDictionary.DATA
        return super().visitDatablock(ctx)

    # def visitDeterm_relation_list(self, ctx: LPhyParser.Determ_relation_listContext):
    #     return super().visitDeterm_relation_list(ctx)
    #
    # def visitDeterm_relation_line(self, ctx: LPhyParser.Determ_relation_lineContext):
    #     return super().visitDeterm_relation_line(ctx)

    def visitModelblock(self, ctx: LPhyParser.ModelblockContext):
        # change _block = MODEL here
        from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary
        self._block = LPhyParserDictionary.MODEL
        return super().visitModelblock(ctx)

    # def visitRelation_list(self, ctx: LPhyParser.Relation_listContext):
    #     return super().visitRelation_list(ctx)
    #
    # def visitRelation(self, ctx: LPhyParser.RelationContext):
    #     return super().visitRelation(ctx)

    def visitVar(self, ctx: LPhyParser.VarContext):
        # TODO may be not required
        id_ = ctx.getChild(0).getText()

        if ctx.getChildCount() > 1:
            # variable of the form NAME '[' range ']'
            o = self.visit(ctx.getChild(2))
            if isinstance(o, RangeList):
                return Var(id_, o, self._parser_dict)
            else:
                raise ParsingException("Expected variable id, or id and range list", ctx)

        return Var(id_, self._parser_dict)

    # return a RangeList function.
    def visitRange_list(self, ctx: LPhyParser.Range_listContext):
        # return self.visitChildren(ctx)
        # TODO re-write
        nodes = []

        for i in range(ctx.getChildCount()):
            # visitExpression
            o = self.visit(ctx.getChild(i))

            if isinstance(o, (Value, range)):
                nodes.append(o)
            elif isinstance(o, DeterministicFunction):
                # f = o
                if isinstance(o.apply().value(), (int, range)):
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
        logging.debug("visitDeterm_relation")

        expr = self.visit(ctx.getChild(2))
        var: Var = self.visit(ctx.children[0])

        if isinstance(expr, DeterministicFunction):
            f = expr
            value = f.apply()
            var.assign(value, f, self._block)
            return value
        elif isinstance(expr, Value):
            value = expr
            var.assign(value, None, self._block)
            return value
        else:
            logging.fatal("in visitDeterm_relation() expecting a function or a value! " + str(expr))

        return None

    def visitStoch_relation(self, ctx: LPhyParser.Stoch_relationContext):
        from .LPhyParserDictionary import LPhyParserDictionary
        if self._block == LPhyParserDictionary.DATA:
            raise ParsingException("Generative distributions are not allowed in the data block! "
                                   "Use model block for Generative distributions.", ctx)

        gen_dist = self.visit(ctx.getChild(2))
        var = self.visit(ctx.getChild(0))

        # TODO
        # if isinstance(gen_dist, VectorizedDistribution) and DataClampingUtils.is_data_clamping(var, parser):
        #     array = self._parser_dict.data_dict[var.get_id()].value()
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
            self._parser_dict.put(variable.get_id(), variable, self._block)
            return variable
        else:
            raise ParsingException("Data clamping requires to data as array object !", ctx)

    def visitLiteral(self, ctx: LPhyParser.LiteralContext):
        text = ctx.getText()
        if text.startswith('"'):
            if text.endswith('"'):
                #TODO make sure text is raw, no \x is added by python
                return Value(None, text[1:-1])
            else:
                raise RuntimeError(f"Attempted to strip quotes, but the string {text} was not quoted.")
        return Value(None, text)  # suppose to be constants

    def visitFloatingPointLiteral(self, ctx: LPhyParser.FloatingPointLiteralContext):
        return super().visitFloatingPointLiteral(ctx)

    def visitIntegerLiteral(self, ctx: LPhyParser.IntegerLiteralContext):
        return super().visitIntegerLiteral(ctx)

    def visitBooleanLiteral(self, ctx: LPhyParser.BooleanLiteralContext):
        return super().visitBooleanLiteral(ctx)

    # An expression_list consists of one or more named_expressions separated by commas.
    def visitExpression_list(self, ctx: LPhyParser.Expression_listContext) -> List[ArgumentValue]:
        # delist and go to visitNamed_expression
        list_values = [self.visit(ctx.getChild(i)) for i in range(0, ctx.getChildCount(), 2)]
        return list_values

    def visitUnnamed_expression_list(self, ctx: LPhyParser.Unnamed_expression_listContext):
        """
        Parse the args of a method call, or the unnamed args in a function.
        """
        values = []
        for i in range(0, ctx.getChildCount(), 2):
            # go to visitExpression
            obj = self.visit(ctx.getChild(i))
            if isinstance(obj, DeterministicFunction):
                value = obj.apply()
                value.set_function(obj)
                values.append(value)
            elif isinstance(obj, Value):
                values.append(obj)
            elif obj is None:
                values.append(None)
            else:
                raise ParsingException("Found a non-value, non-function in unnamed expression list: " + str(obj), ctx)
        return values

    def visitMapFunction(self, ctx: LPhyParser.MapFunctionContext):
        """
        :return: A map function of the name=value pairs contained in this map expression
        """
        ctx1: ParseTree = ctx.getChild(1)
        logging.debug("parsing a map expression: " + ctx1.getText())
        #  ArgumentValue[] parsed by visitExpression_list
        argument_objects = self.visit(ctx1)
        if isinstance(argument_objects, list):
            # A dict containing name=value pairs
            return MapFunction(argument_objects)
        else:
            raise ParsingException(f"Expect a list of ArgumentValue objects, but get {argument_objects} !", ctx1)

    def visitFunction(self, ctx: LPhyParser.FunctionContext):
        """
        Parse lphy functions and return a Value or an Expression
        """
        function_name = ctx.children[0].getText()
        ctx2 = ctx.getChild(2)

        f1 = None
        argument_values = None
        if ctx2.getText() == ")":
            f1 = []
        else:
            # this goes to visitUnnamed_expression_list or visitExpression_list
            argument_objects = self.visit(ctx2)
            if isinstance(argument_objects, list):
                # argument_objects can contain None for optional args
                if all(item is None or isinstance(item, Value) for item in argument_objects):
                    f1 = argument_objects
                elif all(item is None or isinstance(item, ArgumentValue) for item in argument_objects):
                    argument_values = argument_objects
                    f1 = [arg_value.get_value() for arg_value in argument_values if arg_value is not None]

        if function_name in univar_functions:
            expression = None

            # if function_name == "abs":
            #     expression = ExpressionNode1Arg(ctx.getText(), ExpressionNode1Arg.abs(), f1)
            # elif function_name == "acos":
            #     expression = ExpressionNode1Arg(ctx.getText(), ExpressionNode1Arg.acos(), f1)
            # #TODO ...
            # elif function_name == "tanh":
            #     expression = ExpressionNode1Arg(ctx.getText(), ExpressionNode1Arg.tanh(), f1)

            return expression

        # TODO
        # function_classes: List[Function] = ParserUtils.get_function_classes(function_name, argument_values)
        #
        # if function_classes is None:
        #     raise ParsingException(f"Found no implementation for function with name {function_name}", ctx)

        arguments = {}
        if argument_values is None:
            # TODO f1 params not correct for unnamed args in function, e.g. length(x)
            matches = ParserUtils.get_matching_generators(function_name, f1)
        else:
            # rm optional arguments
            arguments_no_optional = [v for v in argument_values if v is not None]
            arguments = {v.get_name(): v.get_value() for v in arguments_no_optional}
            matches = ParserUtils.get_matching_generators(function_name, arguments)

        if len(matches) == 0:
            raise RuntimeError(
                f"Found no function for '{function_name}' matching arguments {str(arguments) if argument_values else str(f1)}")
            # TODO why return null in Java?
        else:
            if len(matches) > 1:
                raise RuntimeError(f"Found {len(matches)} matches for '{function_name}'. Picking first one!")
            generator = matches[0]
            for entry in arguments.items():
                generator.set_input(entry[1])
            return generator.generate()

    def visitMethodCall(self, ctx: LPhyParser.MethodCallContext):
        # TODO
        var = self.visit(ctx.children[0])
        method_name = ctx.children[2].getText()

        if var.is_ranged_var():
            value = get_indexed_value(var.id_, var.range_list).apply()
        else:
            value = self._parser_dict.get_value(var.id_, self._block)

        if value is None:
            raise ParsingException(f"Value {ctx.children[0].getText()} not found for method call {method_name}", ctx)

        argument_values = [] # no args
        ctx2 = ctx.getChild(4)
        if ctx2.getText() != ')':
            # contain args, and visitUnnamed_expression_list
            argument_object = self.visit(ctx2)

            if isinstance(argument_object, list) and all(isinstance(item, Value) for item in argument_object):
                argument_values = argument_object
            elif isinstance(argument_object, list) and all(isinstance(item, ArgumentValue) for item in argument_object):
                argument_values = [value.get_value() for value in argument_object]

        # try:
        return MethodCall(method_name, value, argument_values)
        # except NoSuchMethodException as e:
        #     LoggerUtils.log.severe(f"Method call {method_name} failed on object {value.get_id()}")
        #     raise ParsingException(str(e), ctx)

    def visitDistribution(self, ctx: LPhyParser.DistributionContext):
        name = ctx.getChild(0).getText()
        # go to visitNamed_expression for named args, and return ArgumentValue[]
        f = self.visit(ctx.getChild(2))
        arguments = {}  # map, key is arg name, value is arg value

        for v in f:
            if v is not None:
                if isinstance(v, ArgumentValue):
                    arguments[v.get_name()] = v.get_value()
                else:
                    raise ParsingException(f"Expecting ArgumentValue for {name}: {ctx.getText()}", ctx)
            else:
                raise ParsingException(f"Argument unexpectedly null for {name}: {ctx.getText()}", ctx)

        # get the matched obj(s) of generative distribution given a name, which allows overloading
        matches: List[Generator] = ParserUtils.get_matching_generators(name, arguments)

        if len(matches) == 0:
            raise ParsingException("No generative distribution named " + name +
                                   " found matching arguments " + str(arguments), ctx)
        else:
            if len(matches) > 1:
                logging.warning("Found " + str(len(matches)) + " matches for " + name + ". Picking first one!")
            generator = matches[0]
            # must be done so that Values all know their outputs
            for key, value in arguments.items():
                generator.set_input(value)
            return generator

    def visitNamed_expression(self, ctx: LPhyParser.Named_expressionContext):
        name = ctx.getChild(0).getText()
        # go to visitExpression
        obj = self.visit(ctx.getChild(2))

        # python built-in has to convert to DeterministicFunction, in order to parse args
        if isinstance(obj, DeterministicFunction):
            value = obj.apply()
            value.set_function(obj)
            v = ArgumentValue(name, value, self._parser_dict, self._block)
            return v

        # array construction will return a Value containing list to here
        if isinstance(obj, Value):
            return ArgumentValue(name, obj, self._parser_dict, self._block)

        return obj

    # wrap the array, e.g. [1,2,3], into Value
    def visitArray_construction(self, ctx: LPhyParser.Array_constructionContext):
        if ctx.getChildCount() >= 2:
            s = ctx.getChild(0).getText()
            if s == "[":
                try:
                    arr_str = ctx.getText()
                    # convert to python list
                    lst = ast.literal_eval(arr_str)
                    # TODO literal_eval bug to add \x0 if \ exists, what about other escape char?
                    if isinstance(lst, list):
                        # remove [ ]
                        arr_str2 = ctx.getChild(1).getText()
                        lst = arr_str2.split(",")

                except ValueError:
                    # get unnamed expression list and return Value[],
                    # e.g. vector contains func, e.g. dim = [length(z), length(z[0])];
                    lst = self.visit(ctx.getChild(1))

                return Value(None, lst)

            raise ValueError(f"[ ] are required ! {ctx.getText()}")

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
            if self._parser_dict.has_value(key, self._block):
                return self._parser_dict.get_value(key, self._block)

        expression = None
        if ctx.getChildCount() >= 2:
            s = ctx.getChild(1).getText()
            # getChild(1) to parse the array index, e.g. x[0]
            if s == "[":
                return self._visit_index_range(ctx)

            # TODO: handle built-in functions
            if s in binary_operators:
                # TODO pick the non-working operator, and use if else
                if s == ":":
                    start, end = map(int, ctx.getText().split(":"))
                    # replace Range obj with python range
                    return Value(None, range(start, end + 1))
                else:
                    obj1 = self.visit(ctx.getChild(0))
                    f1 = _get_value_or_function(obj1, ctx, self._parser_dict, self._block)
                    obj2 = self.visit(ctx.getChild(ctx.getChildCount() - 1))
                    f2 = _get_value_or_function(obj2, ctx, self._parser_dict, self._block)
                    expression = f"{f1} {s} {f2}"
                    return eval(expression)

            s = ctx.getChild(0).getText()

            # TODO operator not
            if s == "!":
                f1 = self.visit(ctx.getChild(2))
                expression = f"{s} {f1}"
                return expression
            # Parsing array moves to visit_array_expression

        return super().visitExpression(ctx)

    ### private

    def _visit_index_range(self, ctx):
        """
        :param ctx:
        :return:    a Slice or ElementsAt function, e.g. x[0]
        """
        child = self.visit(ctx.getChild(0))

        array = _get_value_or_function(child, ctx, self._parser_dict, self._block)

        if not isinstance(array.value, (np.ndarray, list)):
            raise ParsingException(f"Expected value {array} to be an array.", ctx)

        # visitRange_list
        range_list = self.visit(ctx.getChild(2))

        return get_indexed_value(array, range_list)
