from abc import ABC
import numpy as np

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class HKY(DeterministicFunction, ABC):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "hky",
                      "description": "The HKY instantaneous rate matrix. "
                                     "Takes a kappa and base frequencies (and optionally a total rate) "
                                     "and produces an HKY85 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, kappa: Value, freq: Value, meanRate: Value = None):
        super().__init__()
        self.kappa = kappa
        self.freq = freq
        self.meanRate = meanRate
        # TODO re-compute Q matrix
        if meanRate is not None:
            raise UnsupportedOperationException(f"meanRate is not implemented yet ! meanRate = {meanRate}")

    def apply(self) -> "Value":
        # not require value
        num_states = 4
        return Value(None, np.zeros((num_states, num_states)), self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        kappa = self.get_param("kappa")
        freq = self.get_param("freq")
        return f"fnHKY(kappa={kappa}, baseFrequencies={freq})"


