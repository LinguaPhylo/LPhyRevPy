import logging
import numpy as np

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


def match(constructor, arguments: List[Argument], init_args, params: Dict[str, Value]) -> bool:
    if not issubclass(constructor.__self__, GenerativeDistribution):
        return False

    if not has_valid_replicates_param(constructor.__name__, params):
        return False

    for i, argument in enumerate(arguments):
        arg_value = init_args[i]

        if argument.name == IID.REPLICATES_PARAM_NAME:
            return False

        if arg_value is None and not argument.optional:
            return False
        elif arg_value is not None and not isinstance(arg_value.value, argument.type):
            return False

    return True


def has_valid_replicates_param(constructor_name, params: Dict[str, Value]) -> bool:
    value = params.get(IID.REPLICATES_PARAM_NAME)
    if value is None:
        return False

    if not isinstance(value.value, int):
        raise ValueError(f"The parameter '{IID.REPLICATES_PARAM_NAME}' must be an integer in {constructor_name}! "
                         f"But it is {value if value else None} ({type(value)})")
    elif value.value < 0:
        raise ValueError(f"The parameter '{IID.REPLICATES_PARAM_NAME}' must >= 0 in {constructor_name}! "
                         f"But it is {value.value}")
    return True


class IID(GenerativeDistribution):

    REPLICATES_PARAM_NAME = "replicates"

    def __init__(self, base_distribution_constructor, init_args, params: Dict[str, Value]):

        self.params = params

        try:
            element_params = {}
            for key, value in params.items():
                if key != self.REPLICATES_PARAM_NAME:
                    element_params[key] = value

            self.base_distribution = base_distribution_constructor(*init_args)
        except Exception as e:
            logging.error("Cannot create instance of %s, check if parameters are valid: %s", base_distribution_constructor.__name__, init_args)
            logging.error(e)


    def size(self) -> int:
        return self.params[IID.REPLICATES_PARAM_NAME].value

    def sample(self) -> RandomVariable:
        size = self.size()
        component_variables = []

        for _ in range(size):
            component_variables.append(self.base_distribution.sample())

        return VectorizedRandomVariable(None, component_variables, self)

    def get_params(self) -> Dict[str, Value]:
        return self.params

    def set_param(self, param_name: str, value: Value):
        self.params[param_name] = value

        if param_name != self.REPLICATES_PARAM_NAME:
            self.base_distribution.set_param(param_name, value)

    def get_name(self) -> str:
        return self.base_distribution.get_name()

    def get_replicates(self) -> Value:
        return self.get_params()[self.REPLICATES_PARAM_NAME]
