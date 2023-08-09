from lphy.core.graphicalmodel.Value import Value


class ValueSet(set):
    def add(self, value):
        if isinstance(value, Value):
            super().add(value)
        else:
            raise ValueError("The value {value} must be instances of the Value class ! But {type(value)}")
