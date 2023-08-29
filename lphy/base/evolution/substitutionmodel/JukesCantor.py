from abc import ABC
from collections import OrderedDict

import numpy as np

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class JukesCantor(DeterministicFunction, ABC):

    generator_info = {"name": "jukesCantor",
                      "description": "The Jukes-Cantor Q matrix construction function. "
                                     "Takes a mean rate and produces a Jukes-Cantor Q matrix."}

    def __init__(self, rate: Value = None):
        super().__init__()
        if rate is not None:
            self.rate = rate
            self.set_param("meanRate", rate);


    def apply(self) -> "Value":
        # not need value
        num_states = 4
        return Value(None, np.zeros((num_states, num_states)), self)

    # def get_params(self):
    #     return OrderedDict([
    #         ("meanRate", self.rate)
    #     ])

