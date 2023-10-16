import numpy as np
from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix
from lphy.core.model.Value import Value


class K80(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "k80",
                      "description": "The K80 instantaneous rate matrix. "
                                     "Takes a kappa and produces a K80 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, kappa: Value, meanRate: Value = None):
        super().__init__(meanRate)
        self.kappa = kappa

    def apply(self) -> "Value":
        kappa = self.kappa.value
        Q = self.k80(kappa)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        kappa = self.get_param("kappa")
        return f"fnK80(kappa={kappa})"

    def k80(self, kappa):
        num_states = 4
        Q = np.zeros((num_states, num_states), dtype=float)
        total_rates = np.zeros(num_states, dtype=float)

        for i in range(num_states):
            for j in range(num_states):
                if i != j:
                    if abs(i - j) == 2:
                        Q[i][j] = kappa
                    else:
                        Q[i][j] = 1.0
                total_rates[i] += Q[i][j]
            Q[i][i] = -total_rates[i]

        freqs = [0.25, 0.25, 0.25, 0.25]  # Frequencies are fixed
        self.normalize(freqs, Q)

        return Q


