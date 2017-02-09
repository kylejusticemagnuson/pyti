import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import exponential_moving_average


class TestExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_ema_period_6(self):
        period = 6
        emas = exponential_moving_average.ema(self.data, period)
        self.assertEqual(len(emas), 127)
        self.assertTrue(np.isnan(emas[4]))
        self.assertAlmostEqual(emas[5], 807.02732709950601)
        self.assertAlmostEqual(emas[9], 811.51167137144193)

    def test_ema_period_8(self):
        period = 8
        emas = exponential_moving_average.ema(self.data, period)
        self.assertEqual(len(emas), 127)
        self.assertTrue(np.isnan(emas[6]))
        self.assertAlmostEqual(emas[7], 809.87511039506569)
        self.assertAlmostEqual(emas[9], 811.09599978863753)

    def test_ema_period_10(self):
        period = 10
        emas = exponential_moving_average.ema(self.data, period)
        self.assertEqual(len(emas), 127)
        self.assertTrue(np.isnan(emas[8]))
        self.assertAlmostEqual(emas[9], 809.99039688880748)

    def test_ema_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            exponential_moving_average.ema(self.data, period)
