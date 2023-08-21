from .GraphicalModelNode import GraphicalModelNode


# Value could be generated from Function
class Value(GraphicalModelNode):
    # must be Generator
    outputs = []

    def __init__(self, value, id_: str = None, function: "Function" = None):
        super().__init__(value)
        # single trailing underscore avoids conflicts with keywords or built-in names
        self.id = id_
        self.function = function

    def set_id(self, id_: str):
        self.id = id_

    def get_id(self):
        return self.id

    # overwrite the default to return the id for a non-anonymous value.
    def get_unique_id(self) -> str:
        if not self.is_anonymous():
            return self.get_id()
        return str(hash(self))

    def add_output(self, gen: "Generator"):
        if gen not in self.outputs:
            self.outputs.append(gen)

    def get_outputs(self):
        return self.outputs

    def get_inputs(self):
        if self.function:
            return [self.function]
        return []

    def get_generator(self):
        return self.function

    # an anonymous value, such as constants
    def is_anonymous(self):
        return self.id is None or self.id.strip() == ""

    # TODO is None value?
    def is_constant(self):
        from .RandomVariable import RandomVariable
        return not isinstance(self, RandomVariable) and not self.get_generator()

    def set_function(self, f):
        self.function = f

    def is_random(self) -> bool:
        from .RandomVariable import RandomVariable
        return isinstance(self, RandomVariable) or (self.function is not None and self.function.has_random_parameters())


