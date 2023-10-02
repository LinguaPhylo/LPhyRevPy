from abc import ABC
import numpy as np

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class F81(DeterministicFunction, ABC):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "f81",
                      "description": "The F81 instantaneous rate matrix. "
                                     "Takes base frequencies and produces an F81 rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, freq: Value, meanRate: Value = None):
        super().__init__()
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

        freq = self.get_param("freq")
        return f"fnF81(baseFrequencies={freq})"


