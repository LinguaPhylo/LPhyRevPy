from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class RandomComposition(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, n: Value, k: Value):
        super().__init__()
        self.n = n  # the sum of the random tuple.
        self.k = k  # the size of the random tuple
        if k.value < 3:
            raise UnsupportedOperationException(f"the size must >= 3 !")

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    # overwrite to F so only print the for loop, without taxa :=
    def has_var_declaration_rev(self):
        return False

    def lphy_to_rev(self, var_name):
        n = self.n.value
        k = self.k.value
        var_nm = "i"
        # see Java version of RandomComposition
        builder = [f"{var_name}_bars[1] <- 0",
                   f"""for ({var_nm} in 2:{k}) {{ {var_name}_bars[{var_nm}] ~ dnUniformInteger(1,{n-1}) }} """,
                   f"{var_name}_bars[{k+1}] <- {n}",
                   f"sort({var_name}_bars)",
                   f"""for ({var_nm} in 1:{k}) {{ {var_name}[{var_nm}] := {var_name}_bars[{var_nm} + 1] - {var_name}_bars[{var_nm}] }} """]
        # TODO check dnUniformInteger bound
        return '\n'.join(builder)
