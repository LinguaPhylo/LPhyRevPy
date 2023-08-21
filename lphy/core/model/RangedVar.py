from lphy.core.model.GraphicalModelNode import GraphicalModelNode


def get_indexed_value(array, range_list):
    if isinstance(array.value(), list):
        if range_list.isRange():
            range_ = range_list.getRangeElement(0)
            return SliceDoubleArray(range_.start(), range_.end(), array)
        elif range_list.isSingle():
            i = range_list.getRangeElement(0)
            return SliceDoubleArray(i, i, array)


class Var:
    def __init__(self, id, graphical_model: GraphicalModelNode, range_list=None):
        self.id = id
        self.graphical_model = graphical_model
        self.range_list = range_list

    def get_id(self):
        return self.id

    def get_range_list(self):
        return self.range_list

    def is_ranged_var(self):
        return self.range_list is not None

    def get_value(self, context):
        val = self.graphical_model.value

        if not self.is_ranged_var():
            return val
        else:
            return get_indexed_value(val, self.range_list).apply()

    def assign(self, value, function, context):
        if not self.is_ranged_var():
            if function is not None:
                value.setFunction(function)
            value.setId(self.id)
            self.graphical_model.put(self.id, value, context)
            return value
        else:
            from lphy.core.error.Errors import UnsupportedOperationException
            raise UnsupportedOperationException("")

            range_ = list(range_list.apply().value())
            max_idx = max(range_)

            if self.graphical_model.hasValue(self.id, context):
                v = self.graphical_model.get_value(self.id, context)
                if isinstance(v.value(), list):
                    current_length = len(v.value())
                    if current_length <= max_idx:
                        new_array = [v.value()[i] if i < current_length else None for i in range_]
                        v.setValue(new_array)
                # Rest of the logic for handling array values

                return v

        # TODO Rest of the logic for assigning values
