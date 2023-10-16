from abc import ABC
import numpy as np

from lphy.base.evolution.substitutionmodel.RateMatrix import RateMatrix
from lphy.core.model.Value import Value


class F81(RateMatrix):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "f81",
                      "description": "The F81 instantaneous rate matrix. "
                                     "Takes base frequencies and produces an F81 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, freq: Value, meanRate: Value = None):
        super().__init__(meanRate)
        self.freq = freq

    def apply(self) -> "Value":
        freq = self.freq.value
        Q = self.f81(freq)
        return Value(None, Q, self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        freq = self.get_param("freq")
        return f"fnF81(baseFrequencies={freq})"

    def f81(self, freqs):
        numStates = 4
        Q = np.zeros((numStates, numStates), dtype=float)
        totalRates = np.zeros(numStates, dtype=float)

        for i in range(numStates):
            for j in range(numStates):
                if i != j:
                    Q[i][j] = freqs[j]
                else:
                    Q[i][i] = 0.0
                totalRates[i] += Q[i][j]
            Q[i][i] = -totalRates[i]

        # Normalizing the rate matrix
        self.normalize(freqs, Q)

        return Q

