from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.simple_moving_average import (
    simple_moving_average as sma
    )
from six.moves import range


def upper_bollinger_band(data, period, std_mult=2.0):
    """
    Upper Bollinger Band.

    Formula:
    u_bb = SMA(t) + STD(SMA(t-n:t)) * std_mult
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    upper_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        upper_bb.append(simple_ma[idx] + std_dev * std_mult)
    upper_bb = fill_for_noncomputable_vals(data, upper_bb)

    return np.array(upper_bb)


def middle_bollinger_band(data, period, std=2.0):
    """
    Middle Bollinger Band.

    Formula:
    m_bb = sma()
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    mid_bb = sma(data, period)

    return mid_bb


def lower_bollinger_band(data, period, std=2.0):
    """
    Lower Bollinger Band.

    Formula:
    u_bb = SMA(t) - STD(SMA(t-n:t)) * std_mult
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    lower_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        lower_bb.append(simple_ma[idx] - std_dev * std)
    lower_bb = fill_for_noncomputable_vals(data, lower_bb)

    return np.array(lower_bb)


def bandwidth(data, period, std=2.0):
    """
    Bandwidth.

    Formula:
    bw = u_bb - l_bb / m_bb
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    bandwidth = ((upper_bollinger_band(data, period, std) -
                 lower_bollinger_band(data, period, std)) /
                 middle_bollinger_band(data, period, std)
                 )

    return bandwidth


def bb_range(data, period, std=2.0):
    """
    Range.

    Formula:
    bb_range = u_bb - l_bb
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    bb_range = (upper_bollinger_band(data, period, std) -
                lower_bollinger_band(data, period, std)
                )
    return bb_range


def percent_bandwidth(data, period, std=2.0):
    """
    Percent Bandwidth.

    Formula:
    %_bw = data() - l_bb() / bb_range()
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    percent_bandwidth = ((np.array(data) -
                         lower_bollinger_band(data, period, std)) /
                         bb_range(data, period, std)
                         )

    return percent_bandwidth


def percent_b(data, period, upper_bb_std=2.0, lower_bb_std=2.0):
    """
    %B.

    Formula:
    %B = ((data - lb) / (ub - lb)) * 100
    """
    lb = lower_bollinger_band(data, period, lower_bb_std)
    ub = upper_bollinger_band(data, period, upper_bb_std)
    percent_b = ((np.array(data) - lb) / (ub - lb)) * 100
    return percent_b
