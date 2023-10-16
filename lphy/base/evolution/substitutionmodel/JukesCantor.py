from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix, jc
from lphy.core.model.Value import Value


class JukesCantor(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "jukesCantor",
                      "description": "The Jukes-Cantor Q matrix construction function. "
                                     "Takes a mean rate and produces a Jukes-Cantor Q matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, meanRate: Value = None):
        super().__init__(meanRate)

    def apply(self) -> "Value":
        num_states = 4
        rate = self.total_rate_default1()
        Q = jc(rate, num_states)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        # if num_states != 4 then use lewisMK
        num_states = 4  # nucleotide
        return f"fnJC({num_states})"


