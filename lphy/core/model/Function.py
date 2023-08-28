from abc import ABC, abstractmethod

from .Generator import Generator, get_argument_code_string


# TODO can this merge with DeterministicFunction?
class Function(Generator, ABC):
    from .ValueCollections import ValueDict
    param_map = ValueDict()

    def __init__(self, id_: str = None):
        super().__init__(id_)

    def specification_operator(self):
        return '='

    def set_param(self, param_name: str, value: "Value"):
        self.param_map[param_name] = value

    def get_params(self):
        return self.param_map

    def code_string(self):
        # TODO modify the code below
        func_class = type(self)

        builder = []
        builder.append(self.get_name())
        builder.append("(")

        constructors = func_class.__init__.__code__.co_varnames

        if len(constructors) == 1:

            # TODO get params from __init__

            parameter_info_list = GeneratorUtils.get_parameter_info(func_class, 0)
            if parameter_info_list:
                param_count = 0

                name = parameter_info_list[0].name()

                if parameter_info_list[0].optional() and self.get_params().get(name) is None:
                    pass  # DO NOTHING - this is an optional parameter with no value
                else:
                    builder.append(get_argument_code_string(name, self.get_params().get(name)))
                    param_count += 1

                for i in range(1, len(parameter_info_list)):
                    name = parameter_info_list[i].name()
                    if parameter_info_list[i].optional() and self.get_params().get(name) is None:
                        pass  # DO NOTHING - this is an optional parameter with no value
                    else:
                        if param_count > 0:
                            builder.append(", ")
                        builder.append(get_argument_code_string(name, self.get_params().get(name)))
                        param_count += 1
        else:
            for name, value in self.get_params().items():
                builder.append(get_argument_code_string(name, value))

        builder.append(")")
        return "".join(builder)


class DeterministicFunction(Function, ABC):

    @abstractmethod
    def apply(self) -> "Value":
        pass

    def generate(self) -> "Value":
        return self.apply()

    # TODO deprecated
    def value(self) -> "Value":
        return self.apply().value()

    # TODO
