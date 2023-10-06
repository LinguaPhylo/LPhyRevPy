from .GraphicalModelNode import GraphicalModelNode
from ..parser.UnicodeConverter import get_canonical


# Value could be generated from Function
class Value(GraphicalModelNode):

    REV_CONST_OP = "<-"

    # must be Generator
    outputs = []

    # only constants have value, variable's value is always None
    def __init__(self, id_: str = None, value=None, function: "Function" = None):
        super().__init__(id_)
        self.value = value
        self.function = function

    # overwrite the default to return the id for a non-anonymous value.
    def get_unique_id(self) -> str:
        if not self.is_anonymous():
            return self.get_id()
        return str(hash(self))

    def add_output(self, gen: "Generator"):
        if gen not in self.outputs:
            self.outputs.append(gen)

    def get_outputs(self):
        return self.outputs

    def get_inputs(self):
        if self.function:
            return [self.function]
        return []

    def get_generator(self) -> "Generator":
        return self.function

    def __str__(self):
        if self.is_anonymous():
            return self.value
        return f"{self.id} = {self.value}"

    def lphy_string(self):
        str_list = []
        generator = self.get_generator()

        from .Generator import Generator
        if generator is not None and isinstance(generator, Generator):
            if not self.is_anonymous():
                # variable id
                str_list.append(self.id)
                str_list.append(" ")
                # = or ~
                str_list.append(generator.specification_operator())
                str_list.append(" ")
            # Function or GenerativeDistribution
            str_list.append(generator.lphy_string())
        elif not self.is_anonymous() and self.value is not None:
            # variable id
            str_list.append(get_canonical(self.id))
            str_list.append(" = ")
            str_list.append(self.value)
        else:
            str_list.append(str(self.value))

        return "".join(str_list)

    def lphy_to_rev(self, var_name):
        builder = []
        str_list = []
        generator = self.get_generator()

        from .Generator import Generator
        if generator is not None and isinstance(generator, Generator):

            id_ = get_canonical(self.id) if self.id is not None else None
            pre_code = generator.rev_code_before(id_)
            if pre_code is not None:
                builder.append(pre_code)

            if not self.is_anonymous() and generator.has_var_declaration_rev():
                # variable id
                str_list.append(id_)
                str_list.append(" ")
                # := or ~
                str_list.append(generator.rev_spec_op())
                str_list.append(" ")

            # check if the parameter Value of generator is Slice
            # from lphy.core.vectorization.function.Slice import Slice
            # if isinstance(generator, Slice):
            #     str_list.append(generator.lphy_to_rev(generator.id))

            # Function or GenerativeDistribution
            gen_str = generator.lphy_to_rev(id_)
            str_list.append(gen_str)

        elif not self.is_anonymous() and self.value is not None:
            # not have generator but have id and value, then it is the constant
            # variable id
            str_list.append(get_canonical(self.id))
            str_list.append(" ")
            # <-
            str_list.append(self.REV_CONST_OP)
            str_list.append(" ")

            # check if a list Value, e.g. [length(z), length(z[0])]
            if isinstance(self.value, list):
                str_list.append("[")
                str_list2 = []
                for elem in self.value:
                    if isinstance(elem, Value):
                        elem_str = elem.lphy_to_rev(elem.get_id())
                        str_list2.append(elem_str)
                    else:
                        str_list2.append(self.value)
                str_list.append(", ".join(str_list2))
                str_list.append("]")
            else:
                str_list.append(self.value)

        else:
            str_list.append(str(self.value))
            #raise RuntimeError(f"Cannot convert the lphy value {str(self.value)} into rev !")

        if None in str_list:
            raise RuntimeError(f"The rev string contains None, check if {generator.__class__} implements lphy_to_rev()!\n"
                               f"Rev string = {format(str_list)}")

        current_line = "".join(str_list)
        builder.append(current_line)

        return '\n'.join(builder)

    # TODO is None value?
    def is_constant(self):
        from .RandomVariable import RandomVariable
        return not isinstance(self, RandomVariable) and not self.get_generator()

    def set_function(self, f):
        self.function = f

    def is_random(self) -> bool:
        from .RandomVariable import RandomVariable
        return isinstance(self, RandomVariable) or (self.function is not None and self.function.has_random_parameters())
