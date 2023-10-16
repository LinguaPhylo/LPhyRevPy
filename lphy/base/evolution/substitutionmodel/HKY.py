import numpy as np
from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix
from lphy.core.model.Value import Value


class HKY(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "hky",
                      "description": "The HKY instantaneous rate matrix. "
                                     "Takes a kappa and base frequencies (and optionally a total rate) "
                                     "and produces an HKY85 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, kappa: Value, freq: Value, meanRate: Value = None):
        super().__init__(meanRate)
        self.kappa = kappa
        self.freq = freq

    def apply(self) -> "Value":
        kappa = self.kappa.value
        freq = self.freq.value
        Q = self.hky(kappa, freq)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        kappa = self.get_param("kappa")
        freq = self.get_param("freq")
        return f"fnHKY(kappa={kappa}, baseFrequencies={freq})"

    def hky(self, kappa, freqs):
        num_states = 4
        Q = np.zeros((num_states, num_states), dtype=float)
        total_rates = np.zeros(num_states, dtype=float)

        for i in range(num_states):
            for j in range(num_states):
                if i != j:
                    if abs(i - j) == 2:
                        Q[i][j] = kappa * freqs[j]
                    else:
                        Q[i][j] = freqs[j]
                else:
                    Q[i][i] = 0.0
                total_rates[i] += Q[i][j]
            Q[i][i] = -total_rates[i]

        self.normalize(freqs, Q)

        return Q


