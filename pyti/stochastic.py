from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.simple_moving_average import (
    simple_moving_average as sma
    )
from six.moves import range


def percent_k(data, period):
    """
    %K.

    Formula:
    %k = data(t) - low(n) / (high(n) - low(n))
    """
    catch_errors.check_for_period_error(data, period)
    percent_k = [((data[idx] - np.min(data[idx+1-period:idx+1])) /
         (np.max(data[idx+1-period:idx+1]) -
          np.min(data[idx+1-period:idx+1]))) for idx in range(period-1, len(data))]
    percent_k = fill_for_noncomputable_vals(data, percent_k)

    return percent_k


def percent_d(data, period):
    """
    %D.

    Formula:
    %D = SMA(%K, 3)
    """
    p_k = percent_k(data, period)
    percent_d = sma(p_k, 3)
    return percent_d
