import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import aroon


class TestAroon(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.aroon_up_expected = \
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, 44.0, 40.0, 36.0, 32.0, 28.000000000000004, 24.0, 20.0,
            16.0, 12.0, 8.0, 4.0, 0.0, 0.0, 92.0, 88.0, 84.0, 80.0, 76.0,
            100.0, 96.0, 100.0, 100.0, 100.0, 96.0, 92.0, 88.0, 84.0, 80.0,
            76.0, 72.0, 68.0, 64.0, 60.0, 56.00000000000001, 52.0, 48.0, 44.0,
            40.0, 36.0, 32.0, 28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0,
            4.0, 0.0, 8.0, 4.0, 0.0, 0.0, 68.0, 64.0, 60.0, 56.00000000000001,
            52.0, 48.0, 44.0, 40.0, 36.0, 32.0, 28.000000000000004, 24.0, 20.0,
            16.0, 12.0, 8.0, 4.0, 0.0, 44.0, 40.0, 36.0, 100.0, 100.0, 96.0,
            92.0, 88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0,
            56.00000000000001, 52.0, 48.0, 44.0, 40.0, 36.0, 32.0,
            28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 0.0, 0.0,
            4.0]

        self.aroon_down_expected = \
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0, 56.00000000000001,
            100.0, 96.0, 92.0, 88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0,
            56.00000000000001, 52.0, 48.0, 44.0, 40.0, 36.0, 32.0,
            28.000000000000004, 24.0, 20.0, 16.0, 12.0, 8.0, 4.0, 0.0, 0.0,
            0.0, 12.0, 8.0, 4.0, 0.0, 0.0, 0.0, 84.0, 80.0, 76.0, 72.0, 68.0,
            100.0, 100.0, 96.0, 92.0, 100.0, 100.0, 96.0, 100.0, 96.0, 92.0,
            88.0, 84.0, 80.0, 76.0, 72.0, 68.0, 64.0, 60.0, 56.00000000000001,
            52.0, 48.0, 44.0, 40.0, 36.0, 32.0, 28.000000000000004, 24.0, 20.0,
            16.0, 12.0, 8.0, 4.0, 0.0, 20.0, 16.0, 12.0, 8.0, 100.0, 100.0,
            100.0, 100.0, 96.0, 100.0, 96.0, 100.0, 100.0, 100.0, 96.0, 100.0,
            96.0, 100.0, 100.0, 100.0, 96.0, 100.0, 96.0]

    def test_aroon_up(self):
        period = 25
        result = aroon.aroon_up(self.data, period)
        np.testing.assert_allclose(result, self.aroon_up_expected, rtol=1e-9,
                                   equal_nan=True)

    def test_aroon_down(self):
        period = 25
        result = aroon.aroon_down(self.data, period)
        np.testing.assert_allclose(result, self.aroon_down_expected, rtol=1e-9,
                                   equal_nan=True)

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
