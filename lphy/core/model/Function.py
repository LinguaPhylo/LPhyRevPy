import inspect
from abc import ABC, abstractmethod

from .Generator import Generator, get_generator_name
from ..parser.LPhyCanonicalBuilder import get_argument_lphy_string
from ..error.Errors import UnsupportedOperationException
from ..parser.argument import ArgumentUtils


# TODO can this merge with DeterministicFunction?
class Function(Generator, ABC):
    from .ValueCollections import ValueDict
    # param_map = ValueDict()

    def __init__(self, id_: str = None):
        super().__init__(id_)

    def specification_operator(self):
        return '='

    # overwrite to <- if the equivalent rev script create a constant var
    def rev_spec_op(self) -> str:
        return ':='


    ### Please note that in Python, defining multiple __init__ methods
    # with different sets of parameters is not recommended,
    # as only the last-defined __init__ method will be effective.
    # If you need to create different constructors with varying parameters,
    # you should consider using class methods or factory functions instead.

    def lphy_string(self):
        builder = [get_generator_name(self), "("]
        arg_str = []

        args_map = self.get_params()
        if args_map:
            for param_name, param in args_map:
                value = self.get_param(param_name)
                # optional argument has a default value, e.g., __init__(param = None)
                if param.default != inspect.Parameter.empty:  # and value is None:
                    pass  # DO NOTHING - this is an optional parameter with no value
                else:
                    arg_str.append(get_argument_lphy_string(param_name, value))

        builder.append(", ".join(arg_str))
        builder.append(")")
        return "".join(builder)


class DeterministicFunction(Function, ABC):

    @abstractmethod
    def apply(self) -> "Value":
        pass

    def generate(self) -> "Value":
        return self.apply()


# Custom decorator to mark functions with @MethodInfo
def method_info(description):
    def decorator(func):
        setattr(func, 'description', description)
        return func
    return decorator
