from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import on_balance_volume


class TestOnBalanceVolume(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.volume = SampleData().get_sample_volume()

        self.obv_expected = [1.0, 1935212.0, 4040894.0, 7328563.0, 5961814.0,
        8499792.0, 10041991.0, 11910243.0, 10805791.0, 9472906.0, 10534598.0,
        11701203.0, 10364618.0, 9016921.0, 10046755.0, 9008059.0, 7960187.0,
        6953575.0, 8204513.0, 6385842.0, 5002723.0, 6013056.0, 7359245.0,
        5972564.0, 4747675.0, 3486613.0, 4947823.0, 3942739.0, 2585554.0,
        3948899.0, 2653191.0, 1238063.0, 43825.0, 1346050.0, 3012655.0,
        4363530.0, 5891625.0, 4202446.0, 1951399.0, 3971579.0, 7488512.0,
        11241009.0, 14734260.0, 16396408.0, 14708033.0, 17165410.0, 18471593.0,
        19542047.0, 18514349.0, 17073444.0, 18363626.0, 17013318.0, 15687924.0,
        14490482.0, 13081558.0, 15098655.0, 13758120.0, 15273459.0, 13314426.0,
        15050305.0, 13992913.0, 15207669.0, 14231707.0, 14997244.0, 13865125.0,
        15324753.0, 16596636.0, 15333055.0, 17931921.0, 19701640.0, 17901986.0,
        15773776.0, 14145174.0, 16049637.0, 17662168.0, 15632753.0, 13898654.0,
        15587127.0, 13868281.0, 16735355.0, 19014409.0, 20576390.0, 18000958.0,
        17387409.0, 16074428.0, 17468602.0, 19099437.0, 17293173.0, 15759494.0,
        17557854.0, 20501743.0, 24190017.0, 27782658.0, 33692267.0, 36790777.0,
        35021708.0, 37014278.0, 38984881.0, 41160097.0, 43510833.0, 41154943.0,
        38912264.0, 43267148.0, 40293662.0, 42088530.0, 43979242.0, 45426858.0,
        43811044.0, 42417174.0, 40917032.0, 38627767.0, 37571400.0, 38683334.0,
        37314353.0, 38222229.0, 36500654.0, 35004539.0, 33840640.0, 34940549.0,
        33726729.0, 34985435.0, 33496223.0, 31836022.0, 30486048.0, 31956328.0,
        30589057.0, 32061789.0]

    def test_obv(self):
        obv = on_balance_volume.on_balance_volume(self.close_data, self.volume)
        np.testing.assert_array_equal(obv, self.obv_expected)

    def test_obv_invalid_data(self):
        self.close_data.append(0)
        with self.assertRaises(Exception) as cm:
            on_balance_volume.on_balance_volume(self.close_data, self.volume)
        expected = "Error: mismatched data lengths, check to ensure that all input data is the same length and valid"
        self.assertEqual(str(cm.exception), expected)
