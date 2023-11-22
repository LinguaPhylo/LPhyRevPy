import inspect
from typing import Any, List, ItemsView

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from lphy.core.parser.UnicodeConverter import get_canonical
from lphy.core.vectorization import VectorMatchUtils
from lphy.core.vectorization.CompoundVectorValue import CompoundVectorValue


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
def find_method(class_obj, method_name, arguments: List[Value]):
    for name, method in inspect.getmembers(class_obj):
        # all lphy method calls are the python functions
        if name == method_name and inspect.isfunction(method):
            sig = inspect.signature(method)
            # deal with vectorized argument whose value is a list, used to be ArrayValue in Java
            for arg in arguments:
                if isinstance(arg.value, list):
                    return None
            # exclude self
            if len(sig.parameters) - 1 == len(arguments):
                return method
    return None


def lphy_to_rev_arg_str(value: Any) -> str:
    if value.is_anonymous():
        return value.lphy_to_rev() # TODO var_name?
    return value.get_id()


class MethodCall(DeterministicFunction):
    OBJECT_PARAM_NAME = "object"
    ARG_PARAM_NAME = "arg"

    # value is the object that the method is being called on,
    # method_name is the method being called,
    # arguments are the arguments of the method call.
    def __init__(self, method_name: str, value: Value, arguments: List[Value]):
        super().__init__()
        self.value = value
        self.method_name = method_name
        self.arguments = arguments
        self.method = None
        # true if the arguments are a vector match for this method
        self.vectorized_arguments = False
        # true if the method is called on the components of a VectorValue
        self.vectorized_object = False

        if value.value is None:
            raise RuntimeError(f"Require the object (id = {value.id}) to locate method call '{method_name}', "
                               f"but it is None !")

        #self.method = find_method(value.value.__class__, self.method_name, self.arguments)
        self._initialize()

    def _initialize(self):
        cls = self.value.value.__class__
        try:
            # Check for exact match
            method = getattr(cls, self.method_name)
            self.method = find_method(cls, self.method_name, self.arguments)
        except AttributeError:
            self.method = None

        if self.method is None:
            if isinstance(self.value, Vector):
                # Check for vectorized object match
                component_class = type(self.value.get_component(0))

                # Check for exact match within vectorized object
                try:
                    self.method = getattr(component_class, self.method_name)
                    vectorized_object = True
                except AttributeError:
                    # Check for doubly vectorized
                    self.method = VectorMatchUtils.get_vector_match(self.method_name, component_class, param_types)
                    if self.method is not None:
                        self.vectorized_object = True
                        self.vectorized_arguments = True

            # If unsuccessful so far
            if self.method is None:
                # Check for vectorized argument match
                self.method = VectorMatchUtils.get_vector_match(self.method_name, self.value, arguments)
                if self.method is not None:
                    self.vectorized_arguments = True

        if self.method is None:
            raise AttributeError(f"Method {self.method_name} not found in {cls} !")

        # cannot set input, it will call value.add_output, so get_sink will wrong if method call on bottom
        #self.set_input(self.value)
        for i, arg in enumerate(self.arguments):
            self.set_input(arg) #TODO need setParam ? Java: setInput(argParamName + i, arguments[i]);

    def apply(self) -> Value:
        if self.vectorized_arguments and self.vectorized_object:
            raise UnsupportedOperationException("Doubly vectorized method calls not supported!")

        argument_values = [arg_val.value if isinstance(arg_val, Value) else arg_val for arg_val in self.arguments]

        if self.vectorized_object:
            size = len(value)
            result_values = []

            for i in range(size):
                result_values.append(ValueCreator.createValue(method.invoke(value[i], argument_values), self))

            return CompoundVectorValue(None, result_values, self)

        if self.vectorized_arguments:
            return self.vector_apply(argument_values) # TODO

        value_obj = self.value.value
        # find method in _initialize()
        if self.method:
            # Call the method with the arguments
            # if self.arguments contains Value, then decompose to v.value
            # TODO vectorization ?
            obj = self.method(value_obj, *argument_values)
        else:
            # Handle the case where the method doesn't exist
            raise RuntimeError(f"Method call {self.method_name} doesn't exist in object {value_obj} !")

        # Unwrap if obj is an instance of Value
        if isinstance(obj, Value):
            obj = obj.value()

        return Value(None, obj, self)

    def vector_apply(self, args: List):
        vector_size = get_vector_size(args)

        is_vector = VectorMatchUtils.is_vector_match(method, [type(arg) for arg in args])

        return_values = []

        call_args = [None] * len(args)

        for i in range(vector_size):
            for j in range(len(args)):
                if is_vector[j]:
                    # TODO implement recycle rule
                    call_args[j] = args[j][i]
                else:
                    call_args[j] = args[j]

            return_values.append(ValueCreator.create_value(method(value.value(), *call_args), self))

        return CompoundVectorValue(None, return_values, self)

    def lphy_to_rev(self, var_name):
        builder = []
        id_ = self.value.get_id()

        if self.value.is_anonymous(): # TODO
            generator = self.value.get_generator()
            if isinstance(generator, ElementsAt) or isinstance(generator, Slice):
                id_ = generator.lphy_to_rev()

        builder.append(f"{get_canonical(id_)}{self.get_name()}(")

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
