from antlr4 import InputStream, CommonTokenStream

from core.parser.LPhyASTVisitor import LPhyASTVisitor
from core.parser.antlr.LPhyLexer import LPhyLexer
from core.parser.antlr.LPhyParser import LPhyParser
from core.graphicalmodel.Value import Value
from core.graphicalmodel.ValueCollections import ValueSet, ValueDict


class LPhyMetaParser:
    # ordered and unchangeable
    DATA = "data"
    MODEL = "model"

    data_dict = ValueDict()
    model_dict = ValueDict()

    data_val_set = ValueSet()
    model_val_set = ValueSet()

    _lines = [str]

    def parse(self, input_string: str, context: str):
        stream = InputStream(input_string)
        # lexer
        lexer = LPhyLexer(stream)
        # get tokens
        tokens = CommonTokenStream(lexer)
        # parser
        parser = LPhyParser(tokens)

        # start rule "input"
        tree = parser.input_()
        # tree = parser.structured_input()

        # AST-specific operations
        visitor = LPhyASTVisitor(self, context)
        # Traverse parse tree, constructing tree along the way
        return visitor.visit(tree)

    def put(self, id_: str, value, context: str):
        if context.lower() == "data":
            self.data_dict[id_] = value
            self.data_val_set.add(value)
        # elif context == "model":
        else:
            self.model_dict[id_] = value
            self.model_val_set.add(value)

    def get_value(self, id_: str, context: str):
        if context.lower() == "data":
            return self.data_dict[id_]
        # context == "model" below
        elif id_ in self.model_dict:
            return self.model_dict[id_]
        else:
            return self.data_dict[id_]

    def has_value(self, id_: str, context: str):
        return bool(self.get_value(id_, context))

    def get_model_sinks(self):
        non_arguments = []

        for val in self.data_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        for val in self.model_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        non_arguments.sort(key=lambda val: val.get_id())

        return non_arguments



