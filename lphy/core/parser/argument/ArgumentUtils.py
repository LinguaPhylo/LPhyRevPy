import inspect
import logging


def get_constructors(cls):
    # Get all members of the class
    members = inspect.getmembers(cls)
    # Filter out the functions to get all constructors __init__
    return [member for name, member in members if name == '__init__' and inspect.isfunction(member)]


def get_arguments_by_index(cls, constructor_index: int):
    init_methods = get_constructors(cls)
    return get_arguments(init_methods[constructor_index])


# return items of param_name, param, which are the argument name of constructor and its object
def get_arguments(constructor, excl_self= True):
    init_signature = inspect.signature(constructor)
    # Get the parameters of the constructor
    parameters = init_signature.parameters

    if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
        # Print the parameters and their default values
        for param_name, param in parameters.items():
            print(f"Parameter: {param_name}, Default Value: {param.default}")

    from collections import OrderedDict
    # Exclude the "self" parameter
    filtered_parameters = OrderedDict((name, param) for name, param in parameters.items() if name != 'self')
    if excl_self:
        return filtered_parameters.items()
    return parameters.items()


def matching_parameter_types(args_map, init_args, params):
    #TODO
    count = 0
    for i, argument_info in enumerate(args_map):
        arg = init_args[i]

        if arg is not None:
            parameter_type = argument_info.type
            value_type = arg.__class__ if lightweight else arg.value().__class__

            if not issubclass(value_type, parameter_type):
                return False
            count += 1
        else:
            if not argument_info.optional:
                return False

    return params is None or count == len(params)


