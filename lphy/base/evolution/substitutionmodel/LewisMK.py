from abc import ABC
import numpy as np

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class LewisMK(DeterministicFunction, ABC):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "lewisMK",
                      "description": "The LewisMK Q matrix construction function. "
                                     "Takes a mean rate and a number of states and produces a LewisMK Q matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, numStates: Value, meanRate: Value = None):
        super().__init__()
        self.numStates = numStates
        self.meanRate = meanRate
        # TODO re-compute Q matrix
        if meanRate is not None:
            raise UnsupportedOperationException(f"meanRate is not implemented yet ! meanRate = {meanRate}")

    def apply(self) -> "Value":
        # not require value
        num_states = self.numStates
        return Value(None, np.zeros((num_states, num_states)), self)

    def lphy_to_rev(self, var_name):
        # lphy mean rate is to normalise rate matrix. Default value is 1.0.
        # mean_rate_name = "meanRate"
        # if self.meanRate is not None:
        #     mean_rate = self.get_param(mean_rate_name)

        num_states = self.numStates
        return f"fnJC({num_states})"


