from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import aroon


class TestAroon(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.aroon_up_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 48.0, 44.0, 40.0, 
        36.0, 32.0, 28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 4.0, 96.0, 92.0, 
        88.0, 84.0, 80.0, 76.0, 100.0, 96.0, 100.0, 100.0, 100.0, 96.0, 92.0, 88.0, 84.0, 
        80.0, 76.0, 72.0, 68.0, 64.0, 60.0, 56.000000000000007, 52.0, 48.0, 44.0, 40.0, 
        36.0, 32.0, 28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 12.0, 8.0, 4.0, 
        4.0, 72.0, 68.0, 64.0, 60.0, 56.000000000000007, 52.0, 48.0, 44.0, 40.0, 36.0, 
        32.0, 28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 48.0, 44.0, 40.0, 
        36.0, 100.0, 100.0, 96.0, 92.0, 88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0, 
        56.000000000000007, 52.0, 48.0, 44.0, 40.0, 36.0, 32.0, 28.000000000000004, 24.0, 
        20.0, 16.0, 12.0, 8.0, 4.0, 4.0, 8.0, 4.0]

        self.aroon_down_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 84.0, 80.0, 76.0, 72.0, 
        68.0, 64.0, 60.0, 56.000000000000007, 100.0, 96.0, 92.0, 88.0, 84.0, 80.0, 76.0, 
        72.0, 68.0, 64.0, 60.0, 56.000000000000007, 52.0, 48.0, 44.0, 40.0, 36.0, 32.0, 
        28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 4.0, 4.0, 16.0, 12.0, 8.0, 
        4.0, 4.0, 4.0, 88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 100.0, 100.0, 96.0, 92.0, 100.0, 
        100.0, 96.0, 100.0, 96.0, 92.0, 88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0, 
        56.000000000000007, 52.0, 48.0, 44.0, 40.0, 36.0, 32.0, 28.000000000000004, 24.0, 
        20.0, 16.0, 12.0, 8.0, 4.0, 24.0, 20.0, 16.0, 12.0, 8.0, 100.0, 100.0, 100.0, 100.0, 
        96.0, 100.0, 96.0, 100.0, 100.0, 100.0, 96.0, 100.0, 96.0, 100.0, 100.0, 100.0, 96.0, 
        100.0, 96.0]

    def test_aroon_up(self):
        period = 25
        aroon_up = aroon.aroon_up(self.data, period)
        np.testing.assert_array_equal(aroon_up, self.aroon_up_expected)

    def test_aroon_down(self):
        period = 25
        aroon_down = aroon.aroon_down(self.data, period)
        np.testing.assert_array_equal(aroon_down, self.aroon_down_expected)

    def test_aroon_up_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            aroon.aroon_up(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_aroon_down_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            aroon.aroon_down(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
