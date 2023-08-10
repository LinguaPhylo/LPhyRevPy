from lphy.core.parser.LPhyMetaParser import LPhyMetaParser


class ArgumentValue:

    def __init__(self, name, value, meta_parser: LPhyMetaParser, block):
        self.name = name
        self.value = value
        if block == LPhyMetaParser.DATA:
            meta_parser.data_val_set.add(value)
        else:
            meta_parser.model_val_set.add(value)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
