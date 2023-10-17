from lphy.core.vectorization.function.RangeList import RangeList
from lphy.core.vectorization.function.Slice import Slice

#TODO
def get_indexed_value(array, range_list: RangeList):
    if isinstance(array.value, list) and len(range_list.range_elements) == 1:
        elem = range_list.get_range_element(0)
        val = elem.value
        if isinstance(val, range):
            from lphy.core.model.Value import Value
            return Slice(Value(None, val.start), Value(None, val.stop), array)
        elif isinstance(val, (int, str)):
            return Slice(elem, elem, array)


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
        from lphy.core.parser.LPhyParserDictionary import LPhyParserDictionary
        if isinstance(self.meta_parser, LPhyParserDictionary):
            val = self.meta_parser.get_value(self.id, block)
            if not self.is_ranged_var():
                return val
            else:
                return get_indexed_value(val, self.range_list).apply()
        else:
            raise RuntimeError("meta_parser is not an instance of LPhyMetaParser !")

    # Assign the given value to this var, and put the result in the graphical model context provided.
    def assign(self, value, function, context):
        if not self.is_ranged_var():
            if value is None:
                raise RuntimeError(f"Cannot assign None to the Var : {self.id}")
            if function is not None:
                value.set_function(function)
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
