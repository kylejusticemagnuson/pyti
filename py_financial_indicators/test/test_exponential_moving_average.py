import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import exponential_moving_average


class TestExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_exponential_moving_average_period_6(self):
        period = 6
        exponential_moving_averages = exponential_moving_average.exponential_moving_average(self.data, period)
        self.assertEqual(len(exponential_moving_averages), 127)
        self.assertTrue(np.isnan(exponential_moving_averages[4]))
        self.assertAlmostEqual(exponential_moving_averages[5], 807.02732709950601)
        self.assertAlmostEqual(exponential_moving_averages[-1], 710.0985836665883)

    def test_exponential_moving_average_period_8(self):
        period = 8
        exponential_moving_averages = exponential_moving_average.exponential_moving_average(self.data, period)
        self.assertEqual(len(exponential_moving_averages), 127)
        self.assertTrue(np.isnan(exponential_moving_averages[6]))
        self.assertAlmostEqual(exponential_moving_averages[7], 809.87511039506569)
        self.assertAlmostEqual(exponential_moving_averages[-1], 712.67957960319632)

    def test_exponential_moving_average_period_10(self):
        period = 10
        exponential_moving_averages = exponential_moving_average.exponential_moving_average(self.data, period)
        self.assertEqual(len(exponential_moving_averages), 127)
        self.assertTrue(np.isnan(exponential_moving_averages[8]))
        self.assertAlmostEqual(exponential_moving_averages[-1], 715.16688890795626)

    def test_exponential_moving_average_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            exponential_moving_average.exponential_moving_average(self.data, period)
