from __future__ import absolute_import
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def linear_weighted_moving_average(data, period):
    """
    Linear Weighted Moving Average.

    Formula:
    LWMA = SUM(DATA[i]) * i / SUM(i)
    """
    catch_errors.check_for_period_error(data, period)

    idx_period = list(range(1, period+1))
    lwma = [(sum([i * idx_period[data[idx-(period-1):idx+1].index(i)]
              for i in data[idx-(period-1):idx+1]])) /
            sum(range(1, len(data[idx+1-period:idx+1])+1)) for idx in range(period-1, len(data))]
    lwma = fill_for_noncomputable_vals(data, lwma)
    return lwma
