from abc import ABC
import numpy as np

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class TN93(DeterministicFunction, ABC):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "tn93",
                      "description": "The TN93 instantaneous rate matrix. "
                                     "Takes kappa1, kappa2 and base frequencies and produces "
                                     "an Tamura-Nei-93 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, kappa1: Value, kappa2: Value, freq: Value, meanRate: Value = None):
        super().__init__()
        self.kappa1 = kappa1
        self.kappa2 = kappa2
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

        kappa1 = self.get_param("kappa1")
        kappa2 = self.get_param("kappa2")
        freq = self.get_param("freq")
        return f"fnTrN(kappa1={kappa1}, kappa2={kappa2}, baseFrequencies={freq})"


