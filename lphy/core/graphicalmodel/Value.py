from lphy.core.graphicalmodel import Function
from lphy.core.graphicalmodel import Generator


class Value:
    # must be Generator
    outputs = []

    def __init__(self, value):
        self.__init__(None, value, None)

    def __init__(self, id_: str, value):
        # single trailing underscore avoids conflicts with keywords or built-in names
        self.__init__(id_, value, None)

    def __init__(self, value, func: Function):
        self.__init__(None, value, func)
        
    def __init__(self, id_: str, value, func: Function):
        self.id = id_
        self.value = value
        self.func = func

    def get_id(self):
        return self.id

    def add_output(self, gen: Generator):
        if gen not in self.outputs:
            self.outputs.append(gen)

    def is_anonymous(self):
        return self.id is None or self.id.strip() == ""


