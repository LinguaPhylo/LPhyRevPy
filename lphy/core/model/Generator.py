from abc import ABC, abstractmethod
from typing import List, Dict

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Value import Value
from lphy.core.model.GraphicalModelNode import GraphicalModelNode
from lphy.core.parser.argument import ArgumentUtils


# this replaces getName()
# get generator name defined for the lphy script,
# if no attr generator_info to define the name, then use the class name
def get_generator_name(generator_class):
    if hasattr(generator_class, 'generator_info'):
        return generator_class.generator_info.get('name')
    elif isinstance(generator_class, type):
        return generator_class.__name__
    else:
        return generator_class.__class__.__name__


# produce the str for named or unnamed args in the lphy script
def get_argument_code_string(name, value):
    prefix = ""
    if not name.isdigit():  # named arg
        prefix = name + "="

    if value is None:
        raise RuntimeError("Value of " + name + " is None!")

    if value.is_anonymous():
        return prefix + value.code_string()
    return prefix + value.get_id()


class Generator(GraphicalModelNode, ABC):

    # return the specification operator, for function '=' and for generative distribution '~'
    @abstractmethod
    def specification_operator(self) -> str:
        pass

    # return a value generated by this generator.
    @abstractmethod
    def generate(self) -> Value:
        pass

    def code_string(self) -> str:
        pass

    # get params from __init__
    # return items of param_name, param
    def get_params(self):
        constructors = ArgumentUtils.get_constructors(self.__class__)
        if len(constructors) == 1:
            return ArgumentUtils.get_arguments(constructors[0])
        else:
            raise RuntimeError(f"{self.__class__.__name__} {self.get_id()} must have 1 and only 1 __init__ !")

    def get_param(self, name_):
        try:
            return self.__getattribute__(name_)
        except AttributeError:
            return None

    def get_type_name(self) -> str:
        return self.__class__.__name__

    def set_input(self, param_name: str, value: Value) -> None:
        # TODO
        # self.set_param(param_name, value)
        value.add_output(self)

    def set_inputs(self, params: Dict[str, Value]) -> None:
        for param_name, value in params.items():
            self.set_input(param_name, value)

    def get_inputs(self):
        return list(self.get_params().values())

    def get_unique_id(self) -> str:
        return str(hash(self))

    def get_param_name(self, value: Value) -> str:
        params = self.get_params()
        for key, val in params.items():
            if val == value:
                return key
        return ""

    def has_random_parameters(self) -> bool:
        for value in self.get_params().values():
            if value is None:
                raise RuntimeError("Unexpected null value in generator " + get_generator_name(self))
            if value.is_random():
                return True
        return False
