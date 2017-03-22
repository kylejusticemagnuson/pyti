import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import relative_strength_index


class TestRelativeStrengthIndex(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_relative_strength_index_period_6(self):
        period = 6
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        self.assertEqual(len(rsi), 127)
        self.assertTrue(np.isnan(rsi[5]))
        self.assertEqual(rsi[6], 91.128696376509808)
        self.assertEqual(rsi[-1], 25.333373455819356)

    def test_relative_strength_index_period_8(self):
        period = 8
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        self.assertEqual(len(rsi), 127)
        self.assertTrue(np.isnan(rsi[7]))
        self.assertEqual(rsi[8], 83.74284752608537)
        self.assertEqual(rsi[-1], 22.415284637880248)

    def test_relative_strength_index_period_10(self):
        period = 10
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        self.assertEqual(len(rsi), 127)
        self.assertTrue(np.isnan(rsi[9]))
        self.assertEqual(rsi[10], 80.382399161864811)
        self.assertEqual(rsi[-1], 21.359400151132036)

    def test_relative_strength_index_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            relative_strength_index.relative_strength_index(self.data, period)
