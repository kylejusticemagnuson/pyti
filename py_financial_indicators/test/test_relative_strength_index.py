import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import relative_strength_index


class TestRelativeStrengthIndex(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_relative_strength_index(self):
        rsi = relative_strength_index.relative_strength_index(self.data, 6)
        print rsi
