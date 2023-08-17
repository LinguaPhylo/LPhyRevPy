import inspect
import pprint

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.parser.argument import ArgumentUtils
from lphy.core.model.Generator import Generator

MAX_UNNAMED_ARGS = 3
REPLICATES_PARAM_NAME = "replicates"  # Replace with the actual parameter name


# TODO
def get_matching_functions(name, arg_values):
    matches = []
    for function_class in LoaderManager.get_function_classes(name):
        matches.extend(_get_function_by_arguments(name, arg_values, function_class))
    return matches


def get_matching_generative_distributions(gene_name, params) -> [Generator]:
    matches = []

    from lphy.base.__loader__ import list_classes_in_package, MODULE_NAME
    found_classes = list_classes_in_package(MODULE_NAME)

    # found_classes return a list of classes
    matching_classes = [obj for obj in found_classes if obj.__name__ == gene_name]
    generators = set(matching_classes)

    if generators is not None:
        for gen_class in generators:
            generator = _get_generator_by_arguments(gene_name, params, gen_class)
            matches.extend(generator)
    else:
        raise RuntimeError(f"No generator with name {gene_name} available.")
    return matches


### private

# Map<String, Value> arguments
def _get_generator_by_arguments(name, params: dict, generator_class: str):
    matches = []

    for constructor in ArgumentUtils.get_constructors(generator_class):
        # args_map -> ItemsView[_KT, _VT_co]
        args_map = ArgumentUtils.get_arguments(constructor)
        arg_values = []

        if _match(params, args_map):

            for param_name, param in args_map.items():
                try:
                    # Value arg
                    arg = params[param_name]
                    arg_values.append(arg)
                except KeyError:
                    if param.default == inspect.Parameter.empty:
                        raise RuntimeError(f"Required argument {param_name} of {name} " +
                                           "looks like optional, so it must have a default value !")
                    # optional, but it must have a default value
                    else:
                        arg_values.append(None)
                        pp = pprint.PrettyPrinter(indent=2)
                        print(f"Optional argument '{param_name}' with default value {param.default} is not in "
                              f"arguments : ")
                        pp.pprint(params)

            matches.append(_construct_generator(name, params, constructor, args_map, arg_values))
    return matches


# Map<String, Value> arguments, args_map -> ItemsView[_KT, _VT_co]
def _match(arguments, args_map):
    required_arguments = set()
    optional_arguments = set()
    keys = set(arguments.keys())

    for param_name, param in args_map.items():
        if param.default == inspect.Parameter.empty:
            required_arguments.add(param)
        else:
            optional_arguments.add(param)

    # return false if not all required arguments are present
    if not keys.issuperset(required_arguments):
        return False

    keys.difference_update(required_arguments)
    keys.difference_update(optional_arguments)
    return len(keys) == 0 or (len(keys) == 1 and REPLICATES_PARAM_NAME in keys)


def _get_function_by_arguments(name, arg_values, generator_class):
    matches = []
    for constructor in generator_class.__init__:
        args_map = ArgumentUtils.get_arguments(constructor)

        if len(arg_values) == len(args_map) and 0 < len(arg_values) <= MAX_UNNAMED_ARGS:
            f = _construct_generator(name, None, constructor, args_map, arg_values)
            if f is not None:
                matches.append(f)
        elif len(arg_values) == 0 and all(x.optional for x in args_map):
            f = _construct_generator(name, None, constructor, args_map, [None] * len(args_map))
            if f is not None:
                matches.append(f)
    return matches


def _construct_generator(name, params, constructor, args_map, arg_values):
    if ArgumentUtils.matching_parameter_types(args_map, arg_values, params):
        return constructor(*arg_values)
    # elif IID.match(constructor, args_map, arg_values, params):
    #     iid = IID(constructor, arg_values, params)
    #     if iid.size() == 1:
    #         return constructor(*arg_values)
    #     return iid
    # elif VectorMatchUtils.vector_match(args_map, arg_values) > 0:
    #     return VectorMatchUtils.vector_generator(constructor, args_map, arg_values)
    else:
        raise UnsupportedOperationException(f"Cannot find a match in '{name}' constructor arguments : " + params)
        #raise RuntimeError(f"ERROR! No match in '{name}' constructor arguments, including vector match! ")
