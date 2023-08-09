from lphy.core.graphicalmodel.Value import Value
from lphy.core.graphicalmodel.ValueDict import ValueDict
from lphy.core.graphicalmodel.Generator import Generator


class Function(Generator):

    param_map = ValueDict()

    def set_param(self, param_name: str, value: Value):
        self.param_map[param_name] = value
