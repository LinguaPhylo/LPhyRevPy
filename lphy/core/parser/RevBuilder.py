from lphy.core.model.Generator import Generator
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.model.Value import Value
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary
from lphy.core.parser.UnicodeConverter import get_canonical


class RevBuilder:
    # Global settings
    NUM_REPLICATES = 2
    NUM_MCMC_ITERATIONS = 1000000  # 1M
    THINNING = 10

    visited = set()

    def __init__(self):
        # TODO merge data_lines with model_lines?
        self.data_lines = []
        self.model_lines = []
        # TODO
        self.move_lines = []
        self.monitors_lines = []

    def get_code(self, parser_dict: LPhyParserDictionary):
        self.visited.clear()
        self.data_lines.clear()
        self.model_lines.clear()

        builder = []
        for value in parser_dict.get_model_sinks():
            self._traverse_graphical_model(value, parser_dict, True)
            if isinstance(value, RandomVariable) and not value.is_anonymous():
                # Since RevBayes model is a graph in which all the model nodes are connected,
                # use any model variable and RevBayes will traverse the graph to copy the entire model
                # into the variable mymodel.
                sink_node_name = get_canonical(value.get_id())
                self.model_lines.append(f"mymodel = model({sink_node_name})")

        if self.data_lines:
            builder += self.data_lines
        if self.model_lines:
            builder += self.model_lines

        if self.move_lines:
            builder += self.move_lines

        return '\n'.join(builder)

    def _traverse_graphical_model(self, node: GraphicalModelNode, parser_dict: LPhyParserDictionary, post: bool):
        if not post:
            self._visit_node(node, parser_dict)
        # TODO Method call is added before the Random Var assigned
        if isinstance(node, Value):
            if node.get_generator() is not None:
                self._traverse_graphical_model(node.get_generator(), parser_dict, post)
        elif isinstance(node, Generator):
            # map value should be Value
            param_map = node.get_params()
            for param_name, param in param_map:
                value = node.get_param(param_name)
                # if optional arg not used, it will be None
                if value is not None:
                    self._traverse_graphical_model(value, parser_dict, post)

            from lphy.core.model.MethodCall import MethodCall
            # traverse the node value of a method call,
            # e.g. TL = ψ.treeLength(); where ψ is value of the graphical model node treeLength()
            if isinstance(node, MethodCall):
                self._traverse_graphical_model(node.value, parser_dict, post)
        else:
            raise RuntimeError("Cannot recognise the node : " + node.__str__())

        if post:
            self._visit_node(node, parser_dict)

    # TODO split lphy inline code into lines of Rev
    def _visit_node(self, node, parser_dict):
        if node not in self.visited:
            if isinstance(node, Value):
                if not node.is_anonymous():
                    # start from named Value, and print the rest
                    str_value = node.lphy_to_rev(None)

                    if isinstance(node, RandomVariable):
                        self.add_moves(node)

                    if parser_dict.is_named_data_value(node):
                        # add data lines
                        self.data_lines.append(str_value)
                    elif parser_dict.is_clamped_variable(node):
                        # data clamping
                        old_id = node.get_id()
                        new_id = old_id + "_clamp"
                        str_clamp = str_value.replace(old_id, new_id)
                        self.model_lines.append(str_clamp)
                        self.model_lines.append(f"{new_id}.clamp({old_id})")
                    else:
                        # add model lines
                        self.model_lines.append(str_value)
                self.visited.add(node)

            elif isinstance(node, Generator):
                # do nothing
                self.visited.add(node)

            else:
                raise RuntimeError("Cannot recognise the node : " + node.__str__())

    def add_moves(self, var: RandomVariable):
        var_name = get_canonical(var.get_id())
        generator = var.get_generator()
        from lphy.base.evolution.likelihood.PhyloCTMC import PhyloCTMC
        from lphy.base.evolution.tree.TimeTree import TimeTree

        # TODO IID
        if not isinstance(generator, PhyloCTMC):
            # https://revbayes.github.io/tutorials/coalescent/constant
            if isinstance(var.value, TimeTree):
                # TODO simulate tree in Coalescent
                n_taxa = var.value.leafCount()
                # add default moves that change the tree
                self.move_lines.append(f"moves.append( mvNarrow({var_name}, weight={n_taxa}) )")
                self.move_lines.append(f"moves.append( mvNNI({var_name}, weight={n_taxa}) )")
                self.move_lines.append(f"moves.append( mvFNPR({var_name}, weight={n_taxa / 4.0}) )")
                self.move_lines.append(f"moves.append( mvSubtreeScale({var_name}, weight={n_taxa / 5.0}) )")
                self.move_lines.append(f"moves.append( mvNodeTimeSlideUniform({var_name}, weight={n_taxa}) )")
                self.move_lines.append(f"moves.append( mvRootTimeScaleBactrian({var_name}, weight={n_taxa / 5.0}) )")
                self.move_lines.append(f"moves.append( mvTreeScale({var_name}, weight={n_taxa / 5.0}) )")

            else:
                # TODO
                mv_params = "lambda=0.1, weight=2.0"
                self.move_lines.append(f"moves.append( mvScale({var_name}, {mv_params}) )")


def get_argument_rev_string(name, value: Value):
    """
    for named arg, for example, (mean=3.0, sd=1.0)
    :param name:   Rev arg name
    :param value:  Value
    :return: the argument string in rev
    """
    prefix = ""
    import re
    pattern = r'^arg_\d+$'  # unnamed arg
    if not re.match(pattern, name):  # named arg
        prefix = name + "="

    if value is None:
        raise RuntimeError("Value of " + name + " is None!")

    if value.is_anonymous():
        # TODO split lphy inline code into lines of Rev
        return prefix + value.lphy_to_rev(None)
    # else value is from a var, then value.get_id() is var name
    return prefix + get_canonical(value.get_id())
