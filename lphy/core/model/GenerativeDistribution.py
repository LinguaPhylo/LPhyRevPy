from .Generator import Generator


class GenerativeDistribution(Generator):

    def specification_operator(self):
        return '~'

    def create_var(self) -> "RandomVariable":
        pass

    def create_var_by_id(self, id_: str) -> "RandomVariable":
        v = self.create_var()
        v.set_id(id_)
        return v

