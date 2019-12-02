from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.simple_moving_average import (
    simple_moving_average as sma
    )
from six.moves import range


def percent_k(high_data, low_data, close_data, period):
    """
    %K.

    Formula:
    %k = data(t) - low(n) / (high(n) - low(n))
    """
    print (len(high_data))
    print (period)
    catch_errors.check_for_period_error(high_data, period)
    catch_errors.check_for_period_error(low_data, period)
    catch_errors.check_for_period_error(close_data, period)
    percent_k = [((close_data[idx] - np.min(low_data[idx+1-period:idx+1])) /
         (np.max(high_data[idx+1-period:idx+1]) -
          np.min(low_data[idx+1-period:idx+1]))) for idx in range(period-1, len(close_data))]
    percent_k = fill_for_noncomputable_vals(close_data, percent_k)

    return percent_k


def percent_d(high_data, low_data, close_data, period):
    """
    %D.

    Formula:
    %D = SMA(%K, 3)
    """
    p_k = percent_k(high_data, low_data, close_data, period)
    percent_d = sma(p_k, 3)
    return percent_d
