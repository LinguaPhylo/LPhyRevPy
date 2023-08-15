
class ValueSet(set):
    def add(self, value):
        from .Value import Value
        if isinstance(value, Value):
            super().add(value)
        else:
            raise ValueError("The value {value} must be instances of the Value class ! But {type(value)}")


class ValueDict(dict):
    def __setitem__(self, key, value):
        from .Value import Value
        if isinstance(value, Value):
            super().__setitem__(key, value)
        else:
            raise ValueError("The value of {key} must be instances of the Value class ! But {type(value)}")
