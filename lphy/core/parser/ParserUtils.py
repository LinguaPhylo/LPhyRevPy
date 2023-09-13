import inspect
import pprint
from typing import List

from lphy.core.parser.argument import ArgumentUtils
from lphy.core.model.Generator import Generator, get_generator_name

MAX_UNNAMED_ARGS = 3
REPLICATES_PARAM_NAME = "replicates"  # Replace with the actual parameter name


# get the matched obj(s) of generative distribution given a name, which allows overloading
def get_matching_generators(gene_name, params) -> [Generator]:
    matches = []

    from lphy.base.__loader__ import list_classes_in_package, MODULE_NAME
    found_classes = list_classes_in_package(MODULE_NAME)

    # found_classes return a list of classes
    generator_classes: List[Generator] = [obj for obj in found_classes if issubclass(obj, Generator)
                                          and obj.__name__ not in ('GenerativeDistribution', 'DeterministicFunction')]

    # look for attr "generator_info" dict, if no exist, then use the class name
    matching_classes = set()
    for gen_class in generator_classes:
        # _get_generator_name to match gene_name
        name = get_generator_name(gen_class)
        if name == gene_name:
            matching_classes.add(gen_class)

    if matching_classes:
        for gen_class in matching_classes:
            generator = _get_generator_by_arguments(gene_name, params, gen_class)
            matches.extend(generator)
    else:
        raise RuntimeError(f'No generator with name "{gene_name}" available.')
    return matches


### private

# find the args matched Generator
# params can be dict or list
def _get_generator_by_arguments(name, params, generator_class):
    matches = []

    for constructor in ArgumentUtils.get_constructors(generator_class):
        # args_map -> ItemsView[_KT, _VT_co]
        args_map = ArgumentUtils.get_arguments(constructor)
        arg_values = []

        #TODO check Generative Dist with unnamed args
        if isinstance(params, dict) and _match(params, args_map):
            # if params is dict, then it is Generative Dist or Func with named args
            for param_name, param in args_map:
                try:
                    # Value arg, if params is empty, return None
                    if params:
                        arg = params[param_name]
                    else:
                        arg = None
                    # if None, all params are optional
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

            generator = _construct_generator(name, params, generator_class, args_map, arg_values)
            matches.append(generator)

        elif isinstance(params, list):
            # if params is list, then it is Func with unnamed args
            #TODO seems working, but need to check and refactor _construct_generator(...)
            # Unnamed args, which use the list params to pass to arg_values
            if len(params) == len(args_map) and 0 < len(params) <= MAX_UNNAMED_ARGS:
                f = _construct_generator(name, None, generator_class, args_map, params)
                if f is not None:
                    matches.append(f)
            # No args, all optional
            elif len(params) == 0 and all(arg[2] for arg in args_map):
                f = _construct_generator(name, None, generator_class, args_map, [])
                if f is not None:
                    matches.append(f)

    return matches


# return if the parsed arguments match the arguments pulled from the constructor
# dict[String, Value] arguments are parsed from lphy script, args_map is from the __init__
def _match(arguments: dict, args_map: dict):
    required_arguments = set()
    optional_arguments = set()
    keys = set(arguments.keys()) if arguments else set()

    for param_name, param in args_map:
        # required argument has no default value, e.g., __init__(param)
        # optional argument has a default value, e.g., __init__(param = None)
        if param.default == inspect.Parameter.empty:
            required_arguments.add(param)
        else:
            optional_arguments.add(param)

    # Extract the parameter names from the Parameter objects
    required_argument_names = {param.name for param in required_arguments}
    # return false if not all required arguments are present
    if not required_argument_names.issubset(keys):
        return False

    keys.difference_update(required_argument_names)
    optional_argument_names = {param.name for param in optional_arguments}
    keys.difference_update(optional_argument_names)
    return len(keys) == 0 or (len(keys) == 1 and REPLICATES_PARAM_NAME in keys)


def _get_function_by_arguments(name, arg_values, generator_class):
    matches = []
    # TODO should only 1 __init__ allowed
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


# return an object of Generator matching the arguments, also including IID and VectorMatch
def _construct_generator(name, params, generator_class, args_map, arg_values):
    # cannot use core.model.Value
    from lphy.core.model.Value import Value
    # arg must be Value obj
    # this causes a bug of matching args, after rm None
    # arg_value_values = [arg for arg in arg_values if arg is not None and isinstance(arg, Value)]
    from lphy.base.distribution.ContinuousDistribution import LogNormal
    # instance = LogNormal(3.0, 1.0)
    # instance = LogNormal(*arg_value_values)
    # constructor = LogNormal

    # TODO
    if True:  #ArgumentUtils.matching_parameter_types(args_map, arg_values, params):
        # tuple unpacking arg_values and use them directly,
        # which supposes to match the constructor parameters in a correct order.
        instance = generator_class(*arg_values)
        return instance

    # TODO
    # elif IID.match(constructor, args_map, arg_values, params):
    #     iid = IID(constructor, arg_values, params)
    #     if iid.size() == 1:
    #         return constructor(*arg_values)
    #     return iid
    # elif VectorMatchUtils.vector_match(args_map, arg_values) > 0:
    #     return VectorMatchUtils.vector_generator(constructor, args_map, arg_values)
    # else:
    #   from lphy.core.error.Errors import UnsupportedOperationException
    #     raise UnsupportedOperationException(f"Cannot find a match in '{name}' constructor arguments : " + params)
    # raise RuntimeError(f"ERROR! No match in '{name}' constructor arguments, including vector match! ")
