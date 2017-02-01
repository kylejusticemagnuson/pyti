import unittest
import numpy as np

from financial_indicators import exponential_moving_average


class TestExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_ema(self):
        period = 6
        emas = exponential_moving_average.ema(self.data, period)
        self.assertEqual(len(emas), 10)
        self.assertTrue(np.isnan(emas[0]))
        self.assertAlmostEqual(emas[6], 5.4189014349564797)
