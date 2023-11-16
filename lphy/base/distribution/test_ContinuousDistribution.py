from math import exp, sqrt, inf
from unittest import TestCase

import numpy as np

from lphy.base.distribution.ContinuousDistribution import LogNormal
from lphy.core.model.Value import Value


class TestLogNormal(TestCase):
    #TODO 1st case is fine, but 2nd log_normal(-1,2) cannot pass
    def test_log_normal(self):
        # Expected log density: dlnorm(seq(0,1,by=.2), 0, 0.25, log = T)
        self.log_normal(0, 0.25, np.array([-inf, -18.6455294, -5.3330631, -1.1093611, 0.2921550, 0.4673558]))
        self.log_normal(-1, 2, np.array([-inf, -0.04907462, -0.69667089, -1.13117154, -1.46438041, -1.73708571]))

    def log_normal(self, meanlog, sdlog, lg_dens_expected, n=100000):
        meanlog_val = Value("meanlog", meanlog)
        sdlog_val = Value("sdlog", sdlog)
        print(f"meanlog = {meanlog}, sdlog = {sdlog}")
        log_normal = LogNormal(meanlog=meanlog_val, sdlog=sdlog_val)

        samples = []
        for _ in range(n):
            var = log_normal.sample()
            samples.append(var.value)
        mean = np.mean(samples)
        median = np.median(samples)
        std = np.std(samples)

        # https://en.wikipedia.org/wiki/Log-normal_distribution
        mean_expected = exp(meanlog + sdlog * sdlog / 2)
        median_expected = exp(meanlog)
        std_expected = sqrt(exp(sdlog * sdlog) - 1) * exp(2 * meanlog + sdlog * sdlog)

        self.assertAlmostEqual(median_expected, median, delta=1e-01,
            msg=f"Expected mean = {median_expected}, but got {median} for {len(samples)} samples !")
        self.assertAlmostEqual(mean_expected, mean, delta=1e-01,
            msg=f"Expected mean = {mean_expected}, but got {mean} for {len(samples)} samples !")
        self.assertAlmostEqual(std_expected, std, delta=1e-01,
            msg=f"Expected std = {std_expected}, but got {std} for {len(samples)} samples !")

        # test_log_density
        # x = 0.0 0.2 0.4 0.6 0.8 1.0
        for i in range(len(lg_dens_expected)):
            x = i / (len(lg_dens_expected) - 1)
            ld = log_normal.log_density(x)
            self.assertAlmostEqual(lg_dens_expected[i], ld, places=5,
                msg=f"Expected log density = {lg_dens_expected[i]} at {x}, but got {ld} from the distribution !")

