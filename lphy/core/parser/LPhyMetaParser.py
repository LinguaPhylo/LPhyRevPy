from antlr4 import InputStream, CommonTokenStream

from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.parser.antlr.LPhyLexer import LPhyLexer
from lphy.core.parser.antlr.LPhyParser import LPhyParser


# store the parsed Values and Generators
class LPhyMetaParser:
    # ordered and unchangeable
    DATA = "data"
    MODEL = "model"

    from lphy.core.model.ValueCollections import ValueSet, ValueDict
    data_dict = ValueDict()
    # the key is the var id, and value is the RandomVar obj
    model_dict = ValueDict()

    data_val_set = ValueSet()
    # all Values and RandomVars
    model_val_set = ValueSet()

    def __init__(self):
        self._lines = []  # TODO where to add lines?

    def parse(self, input_string: str):
        from lphy.core.parser.LPhyASTVisitor import LPhyASTVisitor
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
        visitor = LPhyASTVisitor(self)
        # Traverse parse tree, constructing tree along the way
        return visitor.visit(tree)

    def put(self, id_: str, value, block: str):
        if block.lower() == self.DATA.lower():
            self.data_dict[id_] = value
            self.data_val_set.add(value)
        # elif context == "model":
        else:
            self.model_dict[id_] = value
            self.model_val_set.add(value)

    # only add to *_val_set
    def add_to_value_set(self, value, block: str):
        if block.lower() == self.DATA.lower():
            self.data_val_set.add(value)
        else:
            self.model_val_set.add(value)

    def get_value(self, id_: str, context: str):
        try:
            if context.lower() == self.DATA.lower():
                return self.data_dict[id_]
                # context == "model" below
            elif id_ in self.model_dict:
                return self.model_dict[id_]
            else:
                return self.data_dict[id_]
        except KeyError:
            # In Python, try to access a key that doesn't exist in a dictionary, it will raise a KeyError exception.
            return None

    def has_value(self, id_: str, context: str):
        return bool(self.get_value(id_, context))

    def get_model_sinks(self):
        from lphy.core.model.Value import Value
        non_arguments = []
#TODO this seems wrong
        for val in self.data_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        for val in self.model_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        non_arguments.sort(key=lambda val: val.get_id())

        return non_arguments

    # return true if this is a named value in the data block.
    def is_named_data_value(self, value: Value):
        from lphy.core.model.RandomVariable import RandomVariable
        return (not value.is_anonymous() and not isinstance(value, RandomVariable)
                and self.has_value(value.get_id(), self.DATA))

    def is_clamped(self, id_):
        """
        Check if the given ID is contained in both the data block and the model block,
        and the model ID is a random variable.
        :param id_: A value ID
        :return: True if the ID is clamped, False otherwise
        """
        from lphy.core.model.RandomVariable import RandomVariable
        return (id_ is not None and id_ in self.data_dict.keys() and id_ in self.model_dict.keys() and
                isinstance(self.model_dict[id_], RandomVariable))

    def is_clamped_variable(self, value: Value):
        """
        Check if the given value is a random variable and is clamped.
        :param value: A value object
        :return: True if the value is a clamped random variable, False otherwise
        """
        from lphy.core.model.RandomVariable import RandomVariable
        return isinstance(value, RandomVariable) and self.is_clamped(value.get_id())

    def __str__(self):
        return '\n'.join(self._lines)  # TODO
