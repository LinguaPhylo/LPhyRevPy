import inspect
from typing import Any, List, ItemsView
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


# Function to detect flagged functions in a class
def get_method_calls(class_obj):
    import inspect
    method_calls = []
    for name, method in inspect.getmembers(class_obj, inspect.ismethod):
        # TODO name == "method_info"
        if hasattr(method, 'description'):
            method_calls.append((name, method.flag_name))
    return method_calls


# Function to find a method in a class by name and parameters
def find_method(class_obj, method_name, args):
    for name, method in inspect.getmembers(class_obj):
        # all lphy method calls are the python functions
        if name == method_name and inspect.isfunction(method):
            sig = inspect.signature(method)
            # exclude self
            if len(sig.parameters) - 1 == len(args):
                return method
    return None


def lphy_to_rev_arg_str(value: Any) -> str:
    if value.is_anonymous():
        return value.lphy_to_rev()
    return value.get_id()


class MethodCall(DeterministicFunction):
    OBJECT_PARAM_NAME = "object"
    ARG_PARAM_NAME = "arg"

    # value is the object that the method is being called on,
    # method_name is the method being called,
    # arguments are the arguments of the method call.
    def __init__(self, method_name: str, value: Value, arguments: List[Any]):
        super().__init__()
        self.value = value
        self.method_name = method_name
        self.arguments = arguments
        self.vectorized_arguments = False
        self.vectorized_object = False

        if value.value is None:
            raise RuntimeError(f"method_name = {method_name}, {value.id} = None !")

        self.method = find_method(value.value.__class__, self.method_name, self.arguments)
        self._initialize()

    def _initialize(self):
        # TODO check if method_name and arguments match

        # TODO if (value instanceof Vector)

        # if self.method is None:
        #     self._check_vectorized_matches()

        # value.add_output
        self.set_input(self.value)
        for i, arg in enumerate(self.arguments):
            self.set_input(arg)

    def apply(self) -> Value:
        # TODO  vectorized ...
        # if self.vectorized_object:
        #     size = len(value)
        #     result_values = []
        #
        #     for i in range(size):
        #         result_values.append(ValueCreator.createValue(
        #             method.invoke(value[i], args), self))
        #
        #     return CompoundVectorValue(None, result_values, self)
        #
        # if self.vectorized_arguments:
        #     return self.vector_apply(args)

        # call method
        obj = self.method(self.value, *self.arguments)

        # Unwrap if obj is an instance of Value
        if isinstance(obj, Value):
            obj = obj.value()

        return Value(None, obj, self);

    def vector_apply(self, args: List[Any]) -> Any:
        # Implement vectorized apply logic here
        pass

    def lphy_to_rev(self, var_name):  # TODO
        builder = []
        id = self.value.get_id()

        if self.value.is_anonymous():
            generator = self.value.get_generator()
            if isinstance(generator, ElementsAt) or isinstance(generator, Slice):
                id = generator.lphy_to_rev()

        builder.append(f"{id}{self.get_name()}(")

        if self.arguments:
            builder.append(lphy_to_rev_arg_str(self.arguments[0]))

        for arg in self.arguments[1:]:
            builder.append(", ")
            builder.append(lphy_to_rev_arg_str(arg))

        builder.append(")")
        return "".join(builder)

    def lphy_string(self):
        from lphy.core.error.Errors import UnsupportedOperationException
        raise UnsupportedOperationException("")

    def get_params(self) -> ItemsView:
        params = {self.OBJECT_PARAM_NAME: self.value}
        for i, arg in enumerate(self.arguments):
            params[f"{self.ARG_PARAM_NAME}{i}"] = arg
        return params.items()

    #TODO is this still required?
    def set_param(self, param_name: str, param: Any):
        if param_name == self.OBJECT_PARAM_NAME:
            self.value = param
        elif param_name.startswith(self.ARG_PARAM_NAME):
            index = int(param_name[len(self.ARG_PARAM_NAME):])
            self.arguments[index] = param
        else:
            raise ValueError(f"Param name {param_name} not recognized!")

    def _check_vectorized_matches(self):
        # Implement logic for vectorized matches
        pass

    def is_method_call(o: Any) -> bool:
        return isinstance(o, MethodCall) or (
                isinstance(o, VectorizedFunction) and isinstance(o.getComponentFunction(0), MethodCall)
        )

    def get_name(self) -> str:
        return "." + self.method_name

    def get_description(self) -> str:
        return self.method_info.description()

    def get_vector_size(self, args: List[Any]) -> int:
        # Implement logic to get vector size
        pass
