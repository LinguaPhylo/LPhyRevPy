from lphy.core.model.Generator import Generator
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.model.Value import Value
from lphy.core.parser.LPhyMetaParser import LPhyMetaParser


class CanonicalCodeBuilder:
    def __init__(self):
        self.data_lines = []
        self.model_lines = []

    def get_code(self, meta_parser: LPhyMetaParser):

        self.data_lines.clear()
        self.model_lines.clear()

        builder = []
        for value in meta_parser.get_model_sinks():
            self._traverse_graphical_model(value, meta_parser, True)

        if self.data_lines:
            builder.append("data {")
            for data_line in self.data_lines:
                builder.append("  " + data_line)
            builder.append("}")

        if self.model_lines:
            builder.append("model {")
            for model_line in self.model_lines:
                builder.append("  " + model_line)
            builder.append("}")

        return '\n'.join(builder)

    def _traverse_graphical_model(self, node: GraphicalModelNode, meta_parser: LPhyMetaParser, post: bool):
        if isinstance(node, Value):
            if not post:
                self._visit_node(node, meta_parser)
            if node.get_generator() is not None:
                self._traverse_graphical_model(node.get_generator(), meta_parser, post)
            if post:
                self._visit_node(node, meta_parser)

        elif isinstance(node, Generator):
            if not post:
                self._visit_node(node, meta_parser)
            # map value should be Value
            map = node.get_params()
            for key, value in map.items():
                self._traverse_graphical_model(value, meta_parser, post)
            if post:
                self._visit_node(node, meta_parser)
        else:
            raise RuntimeError("Cannot recognise the node : " + node.__str__())

    def _visit_node(self, node, meta_parser):
        visited = set() # TODO seems not required
        if node not in visited and isinstance(node, Value):
            if not node.is_anonymous():
                str_value = node.code_string()
                if not str_value.endswith(";"):
                    str_value += ";"
                if meta_parser.is_named_data_value(node): #TODO
                    self.data_lines.append(str_value)
                else:
                    self.model_lines.append(str_value)
            visited.add(node)
