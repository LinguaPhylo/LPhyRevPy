from GraphicalModelNode import GraphicalModelNode


class Generator(GraphicalModelNode):

    def get_inputs(self):
        return self.get_params().values()

    def get_params(self) -> dict:
        pass

    def get_name(self) -> str:
        pass

    # return a value generated by this generator.
    def generate(self):
        pass

    def code_string(self) -> str:
        pass

    # return the specification operator, for function '=' and for generative distribution '~'
    def specification_operator(self) -> str:
        pass
