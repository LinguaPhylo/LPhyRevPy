from .GraphicalModelNode import GraphicalModelNode


# Value could be generated from Function
class Value(GraphicalModelNode):
    from .Function import Function
    from .Generator import Generator
    # must be Generator
    outputs = []

    def __init__(self, value, id_: str = None, func: Function = None):
        super().__init__(value)
        # single trailing underscore avoids conflicts with keywords or built-in names
        self.id = id_
        self.func = func

    def set_id(self, id_: str):
        self.id = id_

    def get_id(self):
        return self.id

    def add_output(self, gen: Generator):
        if gen not in self.outputs:
            self.outputs.append(gen)

    # an anonymous value, such as constants
    def is_anonymous(self):
        return self.id is None or self.id.strip() == ""

    # overwrite the default to return the id for a non-anonymous value.
    def get_unique_id(self) -> str:
        if not self.is_anonymous():
            return self.get_id()
        return str(hash(self))
