from abc import ABC
import numpy as np

from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class GTR(DeterministicFunction, ABC):

    # if attr generator_info defines the function name, then use it, otherwise use class name
    generator_info = {"name": "gtr",
                      "description": "The GTR instantaneous rate matrix. "
                                     "Takes relative rates and base frequencies and produces an GTR rate matrix."}

    # The parameter name must be matching with its definition in lphy script, case-sensitive.
    def __init__(self, rates: Value, freq: Value, meanRate: Value = None):
        super().__init__()
        self.rates = rates
        self.freq = freq
        self.meanRate = meanRate
        # TODO re-compute Q matrix
        if meanRate is not None:
            raise UnsupportedOperationException(f"meanRate is not implemented yet ! meanRate = {meanRate}")


    def apply(self) -> "Value":
        # not require value
        num_states = 4  # TODO
        return Value(None, np.zeros((num_states, num_states)), self)

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