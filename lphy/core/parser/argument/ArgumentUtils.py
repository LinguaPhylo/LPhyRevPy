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
def get_arguments(constructor, excl_self=True):
    init_signature = inspect.signature(constructor)
    # Get the parameters of the constructor
    parameters = init_signature.parameters

    if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
        # Print the parameters and their default values
        for param_name, param in parameters.items():
            print(f"Parameter: {param_name}, Default Value: {param.default}")

    from collections import OrderedDict
    # Exclude the "self" parameter
    #filtered_parameters = OrderedDict((name, param) for name, param in parameters.items() if name != 'self')
    filtered_parameters = OrderedDict()
    for param_name, param in parameters.items():
        # Replace "lambda_" because "lambda" is reserved by python
        if param_name == "lambda_":
            # not working after python 3.11
            #filtered_parameters["lambda"] = param.replace(name='lambda')
            filtered_parameters["lambda"] = param
        elif param_name != 'self':
            filtered_parameters[param_name] = param

    if excl_self:
        return filtered_parameters.items()
    #TODO "lambda_" is not changed
    return parameters.items()


# TODO deprecated since python does not need Type?
# TODO only changed names, then what bout unnamed args?
def matching_parameter_types(args_map, init_args, params) -> bool:
    count = 0
    # Parameter objects extracted from the parameters of python class __init__
    for i, (param_name, param) in enumerate(args_map):
        if init_args:
            arg = init_args[i]
            if arg is not None:
                #param_type = param.__class__
                #value_type = arg.value.__class__

                #TODO not sure if it is problematic to check arg_
                if (not param_name.startswith("arg_")) and param_name not in params:
                    return False
                count += 1
            else:
                # param is inspect.Parameter, so it is optional if its value is None not a Value obj
                if param.default is not None:
                    return False

    return params is None or count == len(params)


