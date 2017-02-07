import unittest
import numpy as np

from financial_indicators import simple_moving_average


class TestSimpleMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_sma_period_6(self):
        period = 6
        smas = simple_moving_average.sma(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, 3.5, 4.5, 5.5, 6.5, 7.5]
        self.assertEqual(len(smas), 10)
        self.assertTrue(np.isnan(smas[4]))
        self.assertEqual(smas[5], 3.5)
        self.assertEqual(smas[9], 7.5)

    def test_sma_period_8(self):
        period = 8
        smas = simple_moving_average.sma(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 4.5, 5.5,
        #  6.5]
        self.assertEqual(len(smas), 10)
        self.assertTrue(np.isnan(smas[6]))
        self.assertEqual(smas[7], 4.5)
        self.assertEqual(smas[9], 6.5)
