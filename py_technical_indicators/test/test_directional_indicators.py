import unittest
import numpy as np

from sample_data import SampleData
from technical_indicators import directional_indicators


class TestAccumulationDistribution(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.high_data = SampleData().get_sample_high_data()
        self.low_data = SampleData().get_sample_low_data()
        self.volume = SampleData().get_sample_volume()

        self.positive_directional_movement_expected = [0, 0, 1.9500000000000455, 5.6299999999999955, 0, 0, 0, 0, 0, 0, 6.409999999999968, 0, 0, 0, 2.4200000000000728, 0, 0, 0, 2.2999999999999545, 0, 0, 0, 13.739999999999895, 0, 0, 0, 0, 0.21000000000003638, 0, 0, 0, 0, 0, 0, 0, 0, 6.1299999999999955, 0, 0, 0, 6.659999999999968, 17.519999999999982, 0, 0, 0, 0, 6.67999999999995, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.310000000000059, 0, 2.509999999999991, 0, 1.6499999999999773, 0, 0, 0, 0, 0, 0, 12.670000000000073, 0, 0, 0, 0, 0, 3.599999999999909, 0, 0, 0, 0, 14.670000000000073, 0, 0.36000000000001364, 0, 0, 0, 0, 0, 0, 0, 0, 2.7200000000000273, 0, 2.8799999999999955, 3.6299999999999955, 2.67999999999995, 0, 0, 1.1200000000000045, 1.25, 0, 0, 0, 0, 0, 1.740000000000009, 0, 1.2300000000000182, 0, 0, 0, 0, 0, 0, 0, 2.6299999999999955, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.9099999999999682, 0, 5.7000000000000455]

        self.negative_directional_movement_expected = [0, 10.490000000000009, 0, 0, 0, 2.410000000000082, 2.659999999999968, 2.6900000000000546, 0, 0, 0, 2.1299999999999955, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12.049999999999955, 0, 0, 0, 0, 5.909999999999968, 0, 0, 10.75, 0, 0, 0, 18.519999999999982, 8.470000000000027, 25.730000000000018, 0, 0, 0, 1.7699999999999818, 0, 0, 4.029999999999973, 10.1400000000001, 0, 5.1299999999999955, 0, 7.110000000000014, 0, 0, 5.639999999999986, 0, 0, 0, 0, 8.32000000000005, 0, 0, 0, 0, 0, 0, 0, 4.210000000000036, 0, 7.440000000000055, 0.5, 0, 0, 0.6999999999999318, 0, 0, 0, 2.3899999999999864, 0, 0, 0, 9.950000000000045, 0, 0, 5.080000000000041, 0, 0, 0, 0, 2.4400000000000546, 4.1299999999999955, 0, 0, 2.3799999999999955, 0, 1.0499999999999545, 0, 0, 0, 0, 4.449999999999932, 0, 0, 1.0300000000000864, 0, 0, 1.7900000000000773, 0, 0, 1.580000000000041, 0, 0, 0, 0, 0, 0.2800000000000864, 1.8799999999999955, 0, 0, 0, 0, 0, 0.5199999999999818, 0, 3.0299999999999727, 0, 0, 0, 0, 0, 0]

    def test_positive_directional_movement(self):
        pdm = directional_indicators.positive_directional_movement(self.high_data, self.low_data)
        np.testing.assert_array_equal(pdm, self.positive_directional_movement_expected)

    def test_negative_directional_movement(self):
        ndm = directional_indicators.negative_directional_movement(self.high_data, self.low_data)
        np.testing.assert_array_equal(ndm, self.negative_directional_movement_expected)
