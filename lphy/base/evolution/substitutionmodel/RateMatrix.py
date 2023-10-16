from abc import ABC
import numpy as np

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


def _normalize(freqs, Q, rate):
    """
    :param freqs:
    :param Q:
    :param rate:
    :return: Normalized the rate matrix that has one expected substitution per unit time.
    """
    subst = 0.0
    for i in range(len(Q)):
        subst += -Q[i][i] * freqs[i]

    for i in range(len(Q)):
        for j in range(len(Q)):
            Q[i][j] = rate * (Q[i][j] / subst)


def jc(mean_rate, num_states):
    Q = np.zeros((num_states, num_states), dtype=float)

    for i in range(num_states):
        for j in range(num_states):
            if i != j:
                Q[i][j] = 1.0 / (num_states - 1.0) * mean_rate
            else:
                Q[i][i] = -1.0 * mean_rate

    return Q


class RateMatrix(DeterministicFunction):

    def __init__(self, meanRate: Value = None):
        super().__init__()
        self.meanRate = meanRate

    def normalize(self, freqs, Q):
        _normalize(freqs, Q, self.total_rate_default1())

    def total_rate_default1(self):
        if self.meanRate is not None:
            return self.meanRate.value()
        return 1.0
