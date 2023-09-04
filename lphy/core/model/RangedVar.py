


def get_indexed_value(array, range_list):
    if isinstance(array.value(), list):
        if range_list.isRange():
            range_ = range_list.getRangeElement(0)
            return SliceDoubleArray(range_.start(), range_.end(), array)
        elif range_list.isSingle():
            i = range_list.getRangeElement(0)
            return SliceDoubleArray(i, i, array)


class Var:
    def __init__(self, id_: str, meta_parser: "LPhyMetaParser", range_list=None):
        self.id = id_
        self.meta_parser = meta_parser
        self.range_list = range_list

    def get_id(self):
        return self.id

    def get_range_list(self):
        return self.range_list

    def is_ranged_var(self):
        return self.range_list is not None

    def get_value(self, block: str):
        # self.meta_parser is LPhyMetaParser
        from lphy.core.parser.LPhyMetaParser import LPhyMetaParser
        if isinstance(self.meta_parser, LPhyMetaParser):
            val = self.meta_parser.get_value(self.id, block)
            if not self.is_ranged_var():
                return val
            else:
                return get_indexed_value(val, self.range_list).apply()
        else:
            raise RuntimeError("meta_parser is not an instance of LPhyMetaParser !")

    def assign(self, value, function, context):
        if not self.is_ranged_var():
            if function is not None:
                value.setFunction(function)
            value.set_id(self.id)
            self.meta_parser.put(self.id, value, context)
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
