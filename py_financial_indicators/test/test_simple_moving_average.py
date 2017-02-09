import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import simple_moving_average


class TestSimpleMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_simple_moving_average_period_6(self):
        period = 6
        simple_moving_averages = simple_moving_average.simple_moving_average(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, 3.5, 4.5, 5.5, 6.5, 7.5]
        self.assertEqual(len(simple_moving_averages), 127)
        self.assertTrue(np.isnan(simple_moving_averages[4]))
        self.assertEqual(simple_moving_averages[5], 804.55166666666673)
        self.assertEqual(simple_moving_averages[-1], 712.72500000000002)

    def test_simple_moving_average_period_8(self):
        period = 8
        simple_moving_averages = simple_moving_average.simple_moving_average(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 4.5, 5.5,
        #  6.5]
        self.assertEqual(len(simple_moving_averages), 127)
        self.assertTrue(np.isnan(simple_moving_averages[6]))
        self.assertEqual(simple_moving_averages[7], 806.83875)
        self.assertEqual(simple_moving_averages[-1], 717.29250000000002)

    def test_simple_moving_average_period_10(self):
        period = 10
        simple_moving_averages = simple_moving_average.simple_moving_average(self.data, period)
        # [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        #  np.nan, 5.5]
        self.assertEqual(len(simple_moving_averages), 127)
        self.assertTrue(np.isnan(simple_moving_averages[8]))
        self.assertEqual(simple_moving_averages[-1], 720.97700000000009)

    def test_simple_moving_average_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            simple_moving_average.simple_moving_average(self.data, period)
