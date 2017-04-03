import numpy as np
import catch_errors
from exponential_moving_average import exponential_moving_average as ema


def double_smoothed_stochastic(data, period):
    """
    Double Smoothed Stochastic
    """
    catch_errors.check_for_period_error(data, period)
    lows = map(lambda idx: data[idx] - np.min(data[idx+1-period:idx+1]), range(period-1, len(data)))
    sm_lows = ema(ema(lows, period), period)
    highs = map(lambda idx: np.max(data[idx+1-period:idx+1]) - np.min(data[idx+1-period:idx+1]), range(period-1, len(data)))
    sm_highs = ema(ema(highs, period), period)

    dss = (sm_lows / sm_highs) * 100

    non_computable_values = np.repeat(np.nan, len(data) - len(dss))
    dss = np.append(non_computable_values, dss)
    return dss
