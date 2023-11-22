import logging

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.vectorization import VectorMatchUtils, VectorUtils
from lphy.core.vectorization.IID import IID
from lphy.core.vectorization.VectorizedFunction import VectorizedFunction
from lphy.core.vectorization.VectorizedRandomVariable import VectorizedRandomVariable


class VectorizedDistribution(GenerativeDistribution):
    def __init__(self, base_distribution_constructor, args_map, vector_args):
        super().__init__()
        self.params = {}
        self.base_types = {}

        self.params = VectorMatchUtils.convert_arguments_to_parameter_map(args_map, vector_args)

        # try:
        size = VectorUtils.get_vector_size(args_map, vector_args)
        self.component_distributions = [
            VectorUtils.get_component_generator(base_distribution_constructor, args_map, vector_args, component) for
            component in range(size)]

        # except (AttributeError, TypeError, IndexError) as e:
        #     logging.fatal(f"Error during VectorizedDistribution initialization: {e}")

        for key, value in self.component_distributions[0].get_params().items():
            if value is not None:
                self.base_types[key] = type(value)

    def sample(self, id_: str = None) -> RandomVariable:
        vector_size = VectorUtils.get_vector_size(self.params, self.base_types)
        component_variables = [base_distribution.sample() for base_distribution in self.component_distributions]
        return VectorizedRandomVariable(id_, component_variables, self)

    def get_replicates_value(self):
        for key, value in self.params.items():
            param_generator = value.get_generator()
            if param_generator and self.is_vectorized_parameter(key):
                if isinstance(param_generator, IID):
                    return param_generator.get_replicates()
                elif isinstance(param_generator, VectorizedDistribution):
                    replicates_value = param_generator.get_replicates_value()
                    if replicates_value:
                        return replicates_value
                elif isinstance(param_generator, VectorizedFunction):
                    replicates_value = param_generator.get_replicates_value()
                    if replicates_value:
                        return replicates_value
                else:
                    VectorUtils.get_replicates_value(param_generator, len(self.component_distributions))
        return None

    def is_vectorized_parameter(self, param_name):
        return VectorUtils.is_vectorized_parameter(param_name, self.params.get(param_name), self.base_types)

    def get_to(self, value, narrative):
        replicates_value = self.get_replicates_value()
        if replicates_value:
            return f"{narrative.get_id(replicates_value, False)} - 1"
        return str(value.size() - 1)

    def get_base_distribution(self, component):
        return self.component_distributions[component]

    def get_component_distributions(self):
        return self.component_distributions

    def get_params(self):
        return self.params

    def set_param(self, param_name, value):
        self.params[param_name] = value

        if not self.is_vectorized_parameter(param_name):
            for base_distribution in self.component_distributions:
                base_distribution.set_param(param_name, value)
        else:
            for i in range(len(self.component_distributions)):
                if isinstance(value, CompoundVector):
                    component_value = value.get_component_value(i)
                    if component_value.is_anonymous():
                        component_value.set_id(f"{param_name}{VectorUtils.INDEX_SEPARATOR}{i}")
                    self.component_distributions[i].set_input(param_name, component_value)
                else:
                    slice_value = SliceValue(i, value)
                    self.component_distributions[i].set_input(param_name, slice_value)

    def get_name(self):
        return self.component_distributions[0].get_name()
