import numpy as np
from py_technical_indicators import catch_errors
from py_technical_indicators.function_helper import fill_for_noncomputable_vals
from py_technical_indicators.simple_moving_average import (
    simple_moving_average as sma
    )


def percent_k(data, period):
    """
    %K
    """
    catch_errors.check_for_period_error(data, period)
    percent_k = map(
        lambda idx:
        ((data[idx] - np.min(data[idx+1-period:idx+1])) /
         (np.max(data[idx+1-period:idx+1]) -
          np.min(data[idx+1-period:idx+1]))),
        range(period-1, len(data))
        )
    percent_k = fill_for_noncomputable_vals(data, percent_k)

    return percent_k


def percent_d(data, period):
    """
    %D
    """
    p_k = percent_k(data, period)
    percent_d = sma(p_k, 3)
    return percent_d
