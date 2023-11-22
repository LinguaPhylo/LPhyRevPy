from collections import OrderedDict
from typing import List

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.Value import Value
from lphy.core.vectorization.VectorizedDistribution import VectorizedDistribution
from lphy.core.vectorization.VectorizedFunction import VectorizedFunction


def vector_match(args_map, vector_args: List) -> int:
    vector_matches = 0
    for i in range(len(args_map)):
        argument = args_map.get(i)
        arg_value = vector_args[i]

        if arg_value is None:
            if not argument.optional:
                return 0
        else:
            if argument.type.isAssignableFrom(arg_value.value().getClass()):
                pass  # direct type match
            elif arg_value.value().getClass().isArray() and argument.type.isAssignableFrom(arg_value.value().getClass().getComponentType()):
                vector_matches += 1  # vector match
    return vector_matches


def vector_generator(constructor, args_map, vector_args: List):
    if issubclass(constructor, GenerativeDistribution):
        return VectorizedDistribution(constructor, args_map, vector_args)
    elif issubclass(constructor, DeterministicFunction):
        return VectorizedFunction(constructor, args_map, vector_args)
    else:
        raise ValueError(f"Unexpected Generator class! Expecting a GenerativeDistribution or a DeterministicFunction, "
                         f"but get {constructor}")


def convert_arguments_to_parameter_map(args_map, vector_args: List) -> dict:
    params = OrderedDict()
    for i in range(len(args_map)):
        argument_info = args_map.get(i)
        value = vector_args[i]

        if value is not None:
            params.put(argument_info.name, value)
    return params


def get_vector_match(method_name: str, c, param_types):
    for method in c.getMethods():
        if method.getName() == method_name:
            if any(is_vector_match(method, param_types)):
                return method
    return None


def is_vector_match(method, param_types: List) -> List[bool]:
    method_param_types = method.getParameterTypes()

    if len(method_param_types) == len(param_types):
        vector_match = [is_vector_match(method_param_types[i], param_types[i]) for i in range(len(method_param_types))]
        return vector_match
    raise ValueError("param_types list must be the same length as the method's parameter types list!")


def get_vector_match_by_value(method_name: str, value: Value, arguments: List[Value]):
    param_types = [argument.value().getClass() for argument in arguments]
    c = value.value().getClass()

    try:
        method = c.getMethod(method_name, *param_types)
    except NoSuchMethodException:
        for method in c.getMethods():
            if method.getName() == method_name:
                if any(is_vector_match(method, param_types)):
                    return method
        return None
    return None


def is_vector_match_by_value(method_param_type, param_type: List) -> bool:
    return param_type.isArray() and method_param_type.isAssignableFrom(param_type.getComponentType())
