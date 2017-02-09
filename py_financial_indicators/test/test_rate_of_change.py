import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import rate_of_change


class TestRateOfChange(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_roc_period_6(self):
        period = 6
        rocs = rate_of_change.rate_of_change(self.data, period)
        self.assertTrue(np.isnan(rocs[4]))
        self.assertAlmostEqual(rocs[5], 2.1742696700107143)
        self.assertAlmostEqual(rocs[-1], -2.330858085808587)

    def test_roc_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            rate_of_change.rate_of_change(self.data, period)
