from lphy.core.graphicalmodel import Value


class ValueDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, Value):
            super().__setitem__(key, value)
        else:
            raise ValueError("The value of {key} must be instances of the Value class ! But {type(value)}")
