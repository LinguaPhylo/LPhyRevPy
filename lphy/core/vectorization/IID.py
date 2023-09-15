import logging
from typing import Dict, ItemsView
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.Generator import get_generator_name, Generator
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


# TODO
def iid_match(constructor, args_map, init_args, params: Dict[str, Value]) -> bool:
    if not issubclass(constructor, GenerativeDistribution):
        return False

    if not has_valid_replicates_param(constructor, params):
        return False

    for i, (param_name, param) in enumerate(args_map):
        arg_value = init_args[i]

        # if one of the arguments of the base distribution is replicates than you can't use IID on this base distribution
        if param_name == IID.REPLICATES_PARAM_NAME:
            return False

        if arg_value is None and param.default is not None:
            return False
        elif arg_value is not None and param_name not in params:
            return False

    return True


def has_valid_replicates_param(constructor_name, params: Dict[str, Value]) -> bool:
    value = params.get(IID.REPLICATES_PARAM_NAME)
    if value is None:
        return False

    # if not isinstance(value.value, int):
    #     raise ValueError(f"The parameter '{IID.REPLICATES_PARAM_NAME}' must be an integer in {constructor_name}! "
    #                      f"But it is {value if value else None} ({type(value)})")
    # elif value.value < 0:
    #     raise ValueError(f"The parameter '{IID.REPLICATES_PARAM_NAME}' must >= 0 in {constructor_name}! "
    #                      f"But it is {value.value}")
    return True


class IID(GenerativeDistribution):
    REPLICATES_PARAM_NAME = "replicates"

    def __init__(self, base_distribution_constructor, init_args, params: Dict[str, Value]):

        super().__init__()
        self.params = params

        try:
            element_params = {}
            for key, value in params.items():
                if key != IID.REPLICATES_PARAM_NAME:
                    element_params[key] = value

            self.base_distribution: GenerativeDistribution = base_distribution_constructor(*init_args)
        except Exception as e:
            logging.error("Cannot create instance of %s, check if parameters are valid: %s",
                          base_distribution_constructor.__name__, init_args)
            logging.error(e)

    def size(self) -> int:
        # value is None when replicates = L, where L is a const var
        return self.params[IID.REPLICATES_PARAM_NAME].value

    def sample(self, id_: str = None) -> RandomVariable:
        size = self.size()
        component_variables = []

        if size:
            try:
                s = int(size)
                for i in range(s):
                    component_variables.append(self.base_distribution.sample())
            except ValueError:
                component_variables.append(self.base_distribution.sample())
        else:
            # the case of replicates = L, L is a var and value is None as designed
            component_variables.append(self.base_distribution.sample())

        # must pass id_ here, otherwise cannot put into model/data_dict
        return RandomVariable(id_, component_variables, self)  # TODO still need VectorizedRandomVariable?

    # overwrite to F so only print the for loop, without ~
    def has_var_declaration_rev(self):
        # False, but exclude DiscretizeGamma
        return self.get_name() == "DiscretizeGamma"

    def lphy_to_rev(self, var_name):
        dist_name = self.get_name()
        # TODO how to deal with 0
        replicates = self.get_replicates()

        # exclude DiscretizeGamma because of diff implementation of this model between lphy and rev
        if dist_name == "DiscretizeGamma":
            return self.base_distribution.lphy_to_rev(var_name)

        var_nm = "i"
        # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
        return f"""for ({var_nm} in 1:{replicates}) {{ {var_name}[{var_nm}] {self.base_distribution.rev_spec_op()} {self.base_distribution.lphy_to_rev(var_name)} }} """

    def get_params(self) -> ItemsView:
        return self.params.items()

    def get_name(self) -> str:
        return get_generator_name(self.base_distribution)

    def get_replicates(self):
        size = self.size()
        if size:
            return size
        else:
            return self.get_param(IID.REPLICATES_PARAM_NAME)
