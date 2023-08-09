from lphy.core.graphicalmodel.Value import Value


class LPhyMetaParser:
    # ordered and unchangeable
    DATA = "data"
    MODEL = "model"

    class ValueDict(dict):
        def __setitem__(self, key, value):
            if isinstance(value, Value):
                super().__setitem__(key, value)
            else:
                raise ValueError("The value of {key} must be instances of the Value class ! But {type(value)}")

    data_dict = ValueDict()
    model_dict = ValueDict()

    class ValueSet(set):
        def add(self, value):
            if isinstance(value, Value):
                super().add(value)
            else:
                raise ValueError("The value {value} must be instances of the Value class ! But {type(value)}")

    data_val_set = ValueSet()
    model_val_set = ValueSet()

    def put(self, id_: str, value, context: str):
        if context.lower() == "data":
            self.data_dict[id_] = value
            self.data_val_set.add(value)
        #elif context == "model":
        else:
            self.model_dict[id_] = value
            self.model_val_set.add(value)

    def get_value(self, id_: str, context: str):
        if context.lower() == "data":
            return self.data_dict[id_]
        # context == "model" below
        elif id_ in self.model_dict:
            return self.model_dict[id_]
        else:
            return self.data_dict[id_]

    def has_value(self, id_: str, context: str):
        return bool(self.get_value(id_, context))

    def get_model_sinks(self):
        non_arguments = []

        for val in self.data_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        for val in self.model_dict.values():
            if isinstance(val, Value) and not (val.is_anonymous() and len(val.outputs) == 0):
                non_arguments.append(val)

        non_arguments.sort(key=lambda val: val.get_id())

        return non_arguments



