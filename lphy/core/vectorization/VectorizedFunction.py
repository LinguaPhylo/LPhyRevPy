from collections import OrderedDict

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.vectorization import VectorMatchUtils, VectorUtils
from lphy.core.vectorization.CompoundVectorValue import CompoundVectorValue, CompoundVector
from lphy.core.vectorization.IID import IID


class VectorizedFunction(DeterministicFunction):
    def __init__(self, base_distribution_constructor, args_map, vector_args):
        super().__init__()
        self.params = {}
        self.base_types = OrderedDict()
        self.component_functions = []

        self.params = VectorMatchUtils.convert_arguments_to_parameter_map(args_map, vector_args)

        size = VectorUtils.get_vector_size(args_map, vector_args)
        for component in range(size):
            self.component_functions.add(VectorUtils.get_component_generator(base_distribution_constructor, args_map, vector_args, component))

        self.component_functions.get(0).get_params().forEach(lambda key, value: self.base_types.put(key, value.get_type()))

    def get_component_function(self, component: int):
        return self.component_functions.get(component)

    def apply(self) -> Value:
        vector_size = VectorUtils.get_vector_size(self.params, self.base_types)
        component_values = []

        for i in range(vector_size):
            component_values.add(self.get_component_function(i).apply())

        return CompoundVectorValue(None, component_values, self)

    def get_params(self) -> dict:
        return self.params

    def set_param(self, param_name: str, value: Value):
        self.params[param_name] = value

        if not VectorUtils.is_vectorized_parameter(param_name, value, self.base_types):
            for component_function in self.component_functions:
                component_function.set_param(param_name, value)
        else:
            for i in range(len(self.component_functions)):
                if isinstance(value, CompoundVector):
                    self.component_functions.get(i).set_input(param_name, value.get_component_value(i))
                else:
                    sv = SliceValue(i, value)
                    self.component_functions.get(i).set_input(param_name, sv)


    def get_name(self) -> str:
        return self.component_functions.get(0).get_name()

    def get_replicates_value(self) -> Value:
        from lphy.core.vectorization.VectorizedDistribution import VectorizedDistribution
        for entry in self.get_params().entry_set():
            param_generator = entry.get_value().get_generator()
            if param_generator and self.is_vectorized_parameter(entry.get_key()):
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
                    VectorUtils.get_replicates_value(param_generator, len(self.component_functions))
        return None

    def is_vectorized_parameter(self, param_name: str) -> bool:
        return VectorUtils.is_vectorized_parameter(param_name, self.get_params().get(param_name), self.base_types)

    # def code_string(self) -> str:
    #     return CodeStringUtils.code_string(self.component_functions.get(0), self.get_params())

    # def get_component_functions(self) -> List[DeterministicFunction]:
    #     return Stream.of(self.component_functions).collect(ArrayList::new, List::add, List::addAll)

