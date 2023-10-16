import numpy as np
from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix
from lphy.core.model.Value import Value


class TN93(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "tn93",
                      "description": "The TN93 instantaneous rate matrix. "
                                     "Takes kappa1, kappa2 and base frequencies and produces "
                                     "an Tamura-Nei-93 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, kappa1: Value, kappa2: Value, freq: Value, meanRate: Value = None):
        super().__init__(meanRate)
        self.kappa1 = kappa1
        self.kappa2 = kappa2
        self.freq = freq

    def apply(self) -> "Value":
        kappa1 = self.kappa1.value
        kappa2 = self.kappa2.value
        freq = self.freq.value
        Q = self.tn93(kappa1, kappa2, freq)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        kappa1 = self.get_param("kappa1")
        kappa2 = self.get_param("kappa2")
        freq = self.get_param("freq")
        return f"fnTrN(kappa1={kappa1}, kappa2={kappa2}, baseFrequencies={freq})"

    # freqs = np.array(freqs, dtype=float)  # Convert freqs to NumPy array
    def tn93(self, kappa1, kappa2, freqs):
        num_states = 4
        Q = np.zeros((num_states, num_states), dtype=float)
        total_rates = np.zeros(num_states, dtype=float)

        Q[0, 1] = freqs[1]
        Q[0, 2] = freqs[2] * kappa1
        Q[0, 3] = freqs[3]

        Q[1, 0] = freqs[0]
        Q[1, 2] = freqs[2]
        Q[1, 3] = freqs[3] * kappa2

        Q[2, 0] = freqs[0] * kappa1
        Q[2, 1] = freqs[1]
        Q[2, 3] = freqs[3]

        Q[3, 0] = freqs[0]
        Q[3, 1] = freqs[1] * kappa2
        Q[3, 2] = freqs[2]

        for i in range(num_states):
            for j in range(num_states):
                total_rates[i] += Q[i][j]

        self.normalize(freqs, Q)

        return Q


