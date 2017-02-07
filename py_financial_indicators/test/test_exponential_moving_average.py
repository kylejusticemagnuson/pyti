import unittest
import numpy as np

from financial_indicators import exponential_moving_average


class TestExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_ema_period_6(self):
        period = 6
        emas = exponential_moving_average.ema(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, 4.41890143, 5.41890143,
        #  6.41890143, 7.41890143, 8.41890143]
        self.assertEqual(len(emas), 10)
        self.assertTrue(np.isnan(emas[4]))
        self.assertAlmostEqual(emas[5], 4.41890143)
        self.assertAlmostEqual(emas[9], 8.41890143)

    def test_ema_period_8(self):
        period = 8
        emas = exponential_moving_average.ema(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 5.73701805,
        #  6.73701805, 7.73701805]
        self.assertEqual(len(emas), 10)
        self.assertTrue(np.isnan(emas[6]))
        self.assertAlmostEqual(emas[7], 5.73701805)
        self.assertAlmostEqual(emas[9], 7.73701805)

    def test_ema_period_10(self):
        period = 10
        emas = exponential_moving_average.ema(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        #  np.nan, 7.05308907]
        self.assertEqual(len(emas), 10)
        self.assertTrue(np.isnan(emas[8]))
        self.assertAlmostEqual(emas[9], 7.05308907)

    def test_ema_invalid_period(self):
        period = 11
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            exponential_moving_average.ema(self.data, period)
