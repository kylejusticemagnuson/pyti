from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.simple_moving_average import (
    simple_moving_average as sma
    )
from pyti.typical_price import typical_price


def band_width(high_data, low_data, period):
    """
    Bandwidth.

    Formula:
    BW = SMA(H - L)
    """
    catch_errors.check_for_input_len_diff(high_data, low_data)
    diff = np.array(high_data) - np.array(low_data)
    bw = sma(diff, period)
    return bw


def center_band(close_data, high_data, low_data, period):
    """
    Center Band.

    Formula:
    CB = SMA(TP)
    """
    tp = typical_price(close_data, high_data, low_data)
    cb = sma(tp, period)
    return cb


def upper_band(close_data, high_data, low_data, period):
    """
    Upper Band.

    Formula:
    UB = CB + BW
    """
    cb = center_band(close_data, high_data, low_data, period)
    bw = band_width(high_data, low_data, period)
    ub = cb + bw
    return ub


def lower_band(close_data, high_data, low_data, period):
    """
    Lower Band.

    Formula:
    LB = CB - BW
    """
    cb = center_band(close_data, high_data, low_data, period)
    bw = band_width(high_data, low_data, period)
    lb = cb - bw
    return lb
