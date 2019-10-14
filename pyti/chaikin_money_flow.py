from __future__ import absolute_import

import numpy as np
from pyti import catch_errors
from pyti.exponential_moving_average import exponential_moving_average as ema
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def chaikin_money_flow(close_data, high_data, low_data, volume, period):
    """
    Chaikin Money Flow.

    Formula:
    CMF = SUM[(((Cn - Ln) - (Hn - Cn)) / (Hn - Ln)) * V] / SUM(Vn)
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume)
    catch_errors.check_for_period_error(close_data, period)

    close_data = np.array(close_data)
    high_data = np.array(high_data)
    low_data = np.array(low_data)
    volume = np.array(volume)
    cmf = [sum((((close_data[idx + 1 - period:idx + 1] - low_data[idx + 1 - period:idx + 1]) -
                 (high_data[idx + 1 - period:idx + 1] - close_data[idx + 1 - period:idx + 1])) /
                (high_data[idx + 1 - period:idx + 1] - low_data[idx + 1 - period:idx + 1])) *
               volume[idx + 1 - period:idx + 1]) / sum(volume[idx + 1 - period:idx + 1]) for idx in
           range(period - 1, len(close_data))]
    cmf = fill_for_noncomputable_vals(close_data, cmf)
    return cmf


def chaikin_oscillator(close_data, high_data, low_data, volume, short_period=3, long_period=10):
    """
    Chaikin Oscillator (CHO).
    Chaikin Accumulation Distribution Line (ADL).

    Formula:
    ADL = M(Period-1) + M(Period)
    CHO = ADL = 3day EMA(ADL) - 10day EMA(ADL)
    """
    ac = []
    val_last = 0
    for index in range(0, len(close_data)):
        if high_data[index] != low_data[index]:
            val = val_last + ((close_data[index] - low_data[index]) - (high_data[index] - close_data[index])) / (
                        high_data[index] - low_data[index]) * volume[index]
        else:
            val = val_last
        ac.append(val)
    cho = ema(ac, short_period) - ema(ac, long_period)
    return cho
