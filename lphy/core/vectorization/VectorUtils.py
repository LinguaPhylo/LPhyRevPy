from typing import List, Dict

from lphy.core.model.Generator import Generator
from lphy.core.model.Value import Value
from lphy.core.vectorization.CompoundVectorValue import CompoundVector
from lphy.core.vectorization.IID import IID

INDEX_SEPARATOR = "_"


def is_array_of_type(maybe_array, of_type):
    if maybe_array.value().getClass().isArray():
        component_class = maybe_array.value().getClass().getComponentType()
        return component_class.isAssignableFrom(of_type)
    return False


def is_vectorized_parameter(argument_name: str, value, base_types: Dict) -> bool:
    return is_array_of_type(value, base_types.get(argument_name))


def get_vector_size(params: Dict, base_types: Dict) -> int:
    size = 1
    for entry in params.entrySet():
        name = entry.getKey()
        v = entry.getValue()
        if is_array_of_type(v, base_types.get(name)):
            vector_size = len(v)
            if size == 1:
                size = vector_size
            elif size != vector_size:
                raise RuntimeError("Vector sizes do not match!")
    return size


def get_vector_size_from_arguments(args_map, vector_args) -> int:
    size = -1
    for i in range(len(args_map)):
        argument_info = args_map[i]
        arg_value = vector_args[i]
        if arg_value is None:
            if not argument_info.optional:
                raise ValueError(f"Required parameter {argument_info.name} not included in vector arguments")
        else:
            arg_value_class = arg_value.value().getClass()
            if argument_info.type.isAssignableFrom(arg_value_class):
                pass  # direct type match
            elif arg_value_class.isArray() and argument_info.type.isAssignableFrom(arg_value_class.getComponentType()):
                # vector match
                length = len(arg_value.value())
                if size == -1:
                    size = length
                else:
                    if size != length:
                        raise ValueError("Vector lengths don't match!")
    return size


def get_replicates_value(generator, size: int):
    for entry in generator.getParams().entrySet():
        param_generator = entry.getValue().getGenerator()
        if param_generator is not None:
            if isinstance(param_generator, IID):
                replicates_value = param_generator.get_replicates()
                if replicates_value.value() == size:
                    return replicates_value
            else:
                replicates_value = get_replicates_value(param_generator, size)
                if replicates_value is not None:
                    return replicates_value
    return None


def get_component_generators(constructor, args_map, vector_args) -> List[Generator]:
    size = get_vector_size_from_arguments(args_map, vector_args)
    generators = [get_component_generator(constructor, args_map, vector_args, component) for component in range(size)]
    return generators


def get_component_generator(constructor, args_map, vector_args, component: int) -> Generator:
    args = [None] * len(args_map)
    for i in range(len(args_map)):
        argument_info = args_map[i]
        arg_value = vector_args[i]
        if arg_value is None:
            if not argument_info.optional:
                raise ValueError(f"Required parameter {argument_info.name} not included in vector arguments")
        else:
            arg_value_class = arg_value.value().getClass()
            if argument_info.type.isAssignableFrom(arg_value_class):
                args[i] = vector_args[i]
            elif arg_value_class.isArray() and argument_info.type.isAssignableFrom(arg_value_class.getComponentType()):
                array = arg_value.value()
                length = len(array)
                if length <= component:
                    raise RuntimeError(f"Array {array} is length {length} but attempting to access element {component}")
                if isinstance(arg_value, CompoundVector):
                    args[i] = arg_value.get_component_value(component)
                else:
                    args[i] = Value(arg_value.getId() + INDEX_SEPARATOR + component, array[component])
    return constructor.newInstance(args)



# def get_element_generator(constructor: Constructor, argument_infos: List[Argument], parent_args: List[Object]) -> Generator:
#     args = [None] * len(argument_infos)
#     for i in range(len(argument_infos)):
#         argument_info = argument_infos[i]
#         arg_value = parent_args[i]
#         if arg_value is None:
#             if not argument_info.optional:
#                 raise IllegalArgumentException(f"Required parameter {argument_info.name} not included in arguments")
#         else:
#             arg_value_class = arg_value.value().getClass()
#             if argument_info.type.isAssignableFrom(arg_value_class):
#                 args[i] = parent_args[i]
#     return constructor.newInstance(args)

# def get_component_parameters(params: Map[str, Object], base_types: Map[str, Class], component: int) -> Map[str, Value]:
#     size = 1
#     component_params = TreeMap()
#     for entry in params.entrySet():
#         name = entry.getKey()
#         v = entry.getValue()
#         if is_array_of_type(v, base_types.get(name)):
#             vector_size = len(v)
#             if size == 1:
#                 size = vector_size
#             elif size != vector_size:
#                 raise RuntimeError("Vector sizes do not match!")
#             input_val = v[component]
#             component_params.put(name, Value(f"{v.getId()}{INDEX_SEPARATOR}{component}", input_val))
#         else:
#             component_params.put(name, v)
