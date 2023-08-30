from .GraphicalModelNode import GraphicalModelNode


# Value could be generated from Function
class Value(GraphicalModelNode):
    # must be Generator
    outputs = []

    def __init__(self, id_: str = None, value=None, function: "Function" = None):
        super().__init__(id_)
        self.value = value
        self.function = function

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

    def __str__(self):
        if self.is_anonymous():
            return self.value
        return f"{self.id} = {self.value}"

    def lphy_string(self):
        str_list = []
        generator = self.get_generator()

        from .Generator import Generator
        if generator is not None and isinstance(generator, Generator):
            if not self.is_anonymous():
                # variable id
                str_list.append(self.id)
                str_list.append(" ")
                # = or ~
                str_list.append(generator.specification_operator())
                str_list.append(" ")
            # Function or GenerativeDistribution
            str_list.append(generator.lphy_string())
        else:
            str_list.append(str(self.value))

        return "".join(str_list)

    def lphy_to_rev(self):
        str_list = []
        generator = self.get_generator()

        from .Generator import Generator
        if generator is not None and isinstance(generator, Generator):
            if not self.is_anonymous():
                # variable id
                str_list.append(self.id)
                str_list.append(" ")
                # <- or ~
                str_list.append(generator.rev_spec_op())
                str_list.append(" ")
            # Function or GenerativeDistribution
            str_list.append(generator.lphy_to_rev())
        else:
            str_list.append(str(self.value))

        return "".join(str_list)

    # TODO is None value?
    def is_constant(self):
        from .RandomVariable import RandomVariable
        return not isinstance(self, RandomVariable) and not self.get_generator()

    def set_function(self, f):
        self.function = f

    def is_random(self) -> bool:
        from .RandomVariable import RandomVariable
        return isinstance(self, RandomVariable) or (self.function is not None and self.function.has_random_parameters())
