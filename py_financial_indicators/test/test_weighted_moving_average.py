import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import weighted_moving_average


class TestWeightedMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_weighted_moving_average(self):
        period = 6
        wma = weighted_moving_average.weighted_moving_average(self.data, period)
        self.assertTrue(np.isnan(wma[4]))
        self.assertAlmostEqual(wma[5], 807.08190476)
        self.assertAlmostEqual(wma[-1], 709.82714286)

    def test_wma_period_8(self):
        period = 8
        wma = weighted_moving_average.weighted_moving_average(self.data, period)
        self.assertEqual(len(wma), 127)
        self.assertTrue(np.isnan(wma[6]))
        self.assertAlmostEqual(wma[7], 809.88111111111118)
        self.assertAlmostEqual(wma[-1], 712.59916666666663)

    def test_wma_period_10(self):
        period = 10
        wma = weighted_moving_average.weighted_moving_average(self.data, period)
        self.assertEqual(len(wma), 127)
        self.assertTrue(np.isnan(wma[8]))
        self.assertAlmostEqual(wma[9], 810.30218181818191)
        self.assertAlmostEqual(wma[-1], 715.2269090909092)

    def test_wma_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            wma = weighted_moving_average.weighted_moving_average(self.data, period)
