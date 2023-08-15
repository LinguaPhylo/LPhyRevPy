

class ArgumentValue:

    def __init__(self, name, value, meta_parser: "LPhyMetaParser", block: str):
        self.name = name
        self.value = value
        meta_parser.add_to_value_set(value, block)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
