import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import simple_moving_average


class TestSimpleMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_sma_period_6(self):
        period = 6
        smas = simple_moving_average.sma(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, 3.5, 4.5, 5.5, 6.5, 7.5]
        self.assertEqual(len(smas), 127)
        self.assertTrue(np.isnan(smas[4]))
        self.assertEqual(smas[5], 804.55166666666673)
        self.assertEqual(smas[-1], 712.72500000000002)

    def test_sma_period_8(self):
        period = 8
        smas = simple_moving_average.sma(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 4.5, 5.5,
        #  6.5]
        self.assertEqual(len(smas), 127)
        self.assertTrue(np.isnan(smas[6]))
        self.assertEqual(smas[7], 806.83875)
        self.assertEqual(smas[-1], 717.29250000000002)

    def test_sma_period_10(self):
        period = 10
        smas = simple_moving_average.sma(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        #  np.nan, 5.5]
        self.assertEqual(len(smas), 127)
        self.assertTrue(np.isnan(smas[8]))
        self.assertEqual(smas[-1], 720.97700000000009)

    def test_sma_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            simple_moving_average.sma(self.data, period)
