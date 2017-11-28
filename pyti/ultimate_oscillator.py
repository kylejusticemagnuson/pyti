from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.true_range import true_range
from six.moves import range


def buying_pressure(close_data, low_data):
    """
    Buying Pressure.

    Formula:
    BP = current close - min()
    """
    catch_errors.check_for_input_len_diff(close_data, low_data)
    bp = [close_data[idx] - np.min([low_data[idx], close_data[idx-1]]) for idx in range(1, len(close_data))]
    bp = fill_for_noncomputable_vals(close_data, bp)
    return bp


def avg_helper(close_data, low_data, period):
    catch_errors.check_for_input_len_diff(close_data, low_data)
    catch_errors.check_for_period_error(close_data, period)
    bp = buying_pressure(close_data, low_data)
    tr = true_range(close_data, period)
    avg = [sum(bp[idx+1-period:idx+1]) / sum(tr[idx+1-period:idx+1]) for idx in range(period-1, len(close_data))]
    avg = fill_for_noncomputable_vals(close_data, avg)
    return avg


def average_7(close_data, low_data, period=7):
    """
    Average7.

    Formula:
    AVG7 = SUM(BP) / SUM(TR) for 7 days
    """
    return avg_helper(close_data, low_data, period)


def average_14(close_data, low_data, period=14):
    """
    Averag14.

    Formula:
    AVG14 = SUM(BP) / SUM(TR) for 14 days
    """
    return avg_helper(close_data, low_data, period)


def average_28(close_data, low_data, period=28):
    """
    average_28.

    Formula:
    AVG14 = SUM(BP) / SUM(TR) for 28 days
    """
    return avg_helper(close_data, low_data, period)


def ultimate_oscillator(close_data, low_data):
    """
    Ultimate Oscillator.

    Formula:
    UO = 100 * ((4 * AVG7) + (2 * AVG14) + AVG28) / (4 + 2 + 1)
    """
    a7 = 4 * average_7(close_data, low_data)
    a14 = 2 * average_14(close_data, low_data)
    a28 = average_28(close_data, low_data)
    uo = 100 * ((a7 + a14 + a28) / 7)
    return uo
