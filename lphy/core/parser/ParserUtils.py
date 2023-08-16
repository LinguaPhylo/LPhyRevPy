import inspect
import pprint

from core.error.Errors import UnsupportedOperationException
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


def get_matching_generative_distributions(name, arguments) -> [Generator]:
    matches = []

    generators = LoaderManager.get_all_generative_distribution_classes(name)

    if generators is not None:
        for gen_class in generators:
            matches.extend(_get_generator_by_arguments(name, arguments, gen_class))
    else:
        raise RuntimeError(f"No generator with name {name} available.")
    return matches


### private

# Map<String, Value> arguments
def _get_generator_by_arguments(name, params: dict, generator_class: str):
    matches = []

    for constructor in ArgumentUtils.get_constructors(generator_class):
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


def _match(arguments, args_map):
    required_arguments = set()
    optional_arguments = set()
    keys = set(arguments.keys())

    for argument_inf in argument_info:
        if argument_inf.optional:
            optional_arguments.add(argument_inf.name)
        else:
            required_arguments.add(argument_inf.name)

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
