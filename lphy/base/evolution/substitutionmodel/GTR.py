import numpy as np
from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix
from lphy.core.model.Value import Value


class GTR(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "gtr",
                      "description": "The GTR instantaneous rate matrix. "
                                     "Takes relative rates and base frequencies and produces an GTR rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, rates: Value, freq: Value, meanRate: Value = None):
        super().__init__(meanRate)
        self.rates = rates
        self.freq = freq

    def apply(self) -> "Value":
        rates = self.rates.value
        freq = self.freq.value
        Q = self.gtr(rates, freq)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0
        mean_rate_name = "meanRate"
        if self.meanRate is not None:
            mean_rate = self.get_param(mean_rate_name)

        rates_name = "exchangeRates"
        freq_name = "baseFrequencies"
        rates = self.get_param("rates")
        freq = self.get_param("freq")
        from lphy.core.parser.RevBuilder import get_argument_rev_string
        return f"fnGTR({get_argument_rev_string(rates_name, rates)}, {get_argument_rev_string(freq_name, freq)})"

    def gtr(self, rates, freqs):
        num_states = 4
        Q = np.zeros((num_states, num_states), dtype=float)
        total_rates = np.zeros(num_states, dtype=float)
        upper = 0

        for i in range(num_states):
            for j in range(i + 1, num_states):
                Q[i][j] = rates[upper] * freqs[j]
                Q[j][i] = rates[upper] * freqs[i]
                upper += 1

        for i in range(num_states):
            total_rate = 0.0
            for j in range(num_states):
                if j != i:
                    total_rate += Q[i][j]
            Q[i][i] = -total_rate

        self.normalize(freqs, Q)

        return Q
