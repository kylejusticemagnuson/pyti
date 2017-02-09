import unittest
import numpy as np

from sample_data import SampleData
from financial_indicators import acceleration_bands


class TestAccelerationBands(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_stock_data()

    def test_upper_band(self):
        period = 6
        upper_band = acceleration_bands.upper_band(self.data, period)
        self.assertTrue(np.isnan(upper_band[4]))
        self.assertAlmostEqual(upper_band[5], 1924.2185770864301)
        self.assertAlmostEqual(upper_band[-1], 1832.3919104197635)

    def test_middle_band(self):
        period = 6
        middle_band = acceleration_bands.middle_band(self.data, period)
        self.assertTrue(np.isnan(middle_band[4]))
        self.assertAlmostEqual(middle_band[5], 804.55166667)
        self.assertAlmostEqual(middle_band[-1], 712.725)

    def test_lower_band(self):
        period = 6
        lower_band = acceleration_bands.lower_band(self.data, period)
        self.assertTrue(np.isnan(lower_band[4]))
        self.assertAlmostEqual(lower_band[5], 339.13475624690346)
        self.assertAlmostEqual(lower_band[-1], 247.30808958023675)
