from lphy.core.model.Generator import Generator
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.model.Value import Value
from lphy.core.parser.LPhyMetaParser import LPhyMetaParser
from lphy.core.parser.UnicodeConverter import get_canonical


class RevBuilder:
    visited = set()

    def __init__(self):
        #TODO merge data_lines with model_lines?
        self.data_lines = []
        self.model_lines = []
        #TODO
        self.mcmc_lines = []

    def get_code(self, meta_parser: LPhyMetaParser):
        self.visited.clear()
        self.data_lines.clear()
        self.model_lines.clear()

        builder = []
        for value in meta_parser.get_model_sinks():
            self._traverse_graphical_model(value, meta_parser, True)

        # TODO
        if self.data_lines:
            for data_line in self.data_lines:
                builder.append(data_line)

        if self.model_lines:
            for model_line in self.model_lines:
                builder.append(model_line)
        return '\n'.join(builder)

    def _traverse_graphical_model(self, node: GraphicalModelNode, meta_parser: LPhyMetaParser, post: bool):
        if not post:
            self._visit_node(node, meta_parser)

        if isinstance(node, Value):
            if node.get_generator() is not None:
                self._traverse_graphical_model(node.get_generator(), meta_parser, post)
        elif isinstance(node, Generator):
            # map value should be Value
            param_map = node.get_params()
            for param_name, param in param_map:
                value = node.get_param(param_name)
                # if optional arg not used, it will be None
                if value is not None:
                    self._traverse_graphical_model(value, meta_parser, post)
        else:
            raise RuntimeError("Cannot recognise the node : " + node.__str__())

        if post:
            self._visit_node(node, meta_parser)

    #TODO split lphy inline code into lines of Rev
    def _visit_node(self, node, meta_parser):
        if node not in self.visited:
            if isinstance(node, Value):
                if not node.is_anonymous():
                    # start from named Value, and print the rest
                    str_value = node.lphy_to_rev()
                    if meta_parser.is_named_data_value(node):
                        self.data_lines.append(str_value)
                    else:
                        self.model_lines.append(str_value)
                self.visited.add(node)

            elif isinstance(node, Generator):
                # do nothing
                self.visited.add(node)

            else:
                raise RuntimeError("Cannot recognise the node : " + node.__str__())


def get_argument_rev_string(name, value: Value):
    prefix = ""
    if not name.isdigit():  # named arg
        prefix = name + "="

    if value is None:
        raise RuntimeError("Value of " + name + " is None!")

    if value.is_anonymous():
        # TODO split lphy inline code into lines of Rev
        return prefix + value.lphy_to_rev()
    return prefix + get_canonical(value.get_id())
