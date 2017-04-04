import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import aroon


class TestAroon(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.aroon_up_period_6_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0,
        100.0, 0.0, 100.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0,
        100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0,
        100.0, 0.0, 0.0, 0.0, 100.0, 100.0, 100.0, 100.0, 0.0, 0.0, 100.0, 0.0,
        100.0, 100.0, 100.0, 0.0, 100.0, 0.0, 100.0, 100.0]

        self.aroon_up_period_14_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0,
        0.0, 100.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 100.0, 100.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 100.0, 0.0, 0.0, 0.0, 100.0,
        100.0, 100.0, 100.0, 0.0, 0.0, 100.0, 0.0]

        self.aroon_down_period_6 = [np.nan, np.nan, np.nan, np.nan, np.nan,
        100.0, 100.0, 100.0, 0.0, 100.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 100.0, 0.0, 0.0, 0.0,
        100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0,
        100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 100.0, 100.0,
        100.0, 100.0, 100.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0]

        self.aroon_down_period_14 = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 100.0,
        100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 100.0, 100.0, 100.0, 0.0, 0.0, 0.0, 100.0, 100.0, 100.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 100.0, 0.0, 0.0, 0.0, 100.0, 100.0, 100.0, 100.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0]

    def test_aroon_up_period_6(self):
        period = 6
        aroon_up = aroon.aroon_up(self.data, period)
        np.testing.assert_array_equal(aroon_up, self.aroon_up_period_6_expected)

    def test_aroon_up_period_14(self):
        period = 14
        aroon_up = aroon.aroon_up(self.data, period)
        np.testing.assert_array_equal(aroon_up, self.aroon_up_period_14_expected)

    def test_aroon_down_period_6(self):
        period = 6
        aroon_down = aroon.aroon_down(self.data, period)
        np.testing.assert_array_equal(aroon_down, self.aroon_down_period_6)

    def test_aroon_down_period_14(self):
        period = 14
        aroon_down = aroon.aroon_down(self.data, period)
        np.testing.assert_array_equal(aroon_down, self.aroon_down_period_14)

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
