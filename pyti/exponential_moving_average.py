from __future__ import absolute_import
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def exponential_moving_average(data, period):
    """
    Exponential Moving Average.

    Formula:
    p0 + (1 - w) * p1 + (1 - w)^2 * p2 + (1 + w)^3 * p3 +...
                /   1 + (1 - w) + (1 - w)^2 + (1 - w)^3 +...

    where: w = 2 / (N + 1)
    """
    catch_errors.check_for_period_error(data, period)
    emas = [exponential_moving_average_helper(
            data[idx - period + 1:idx + 1], period) for idx in range(period - 1, len(data))]
    emas = fill_for_noncomputable_vals(data, emas)
    return emas


def exponential_moving_average_helper(data, period):
    w = 2 / float(period + 1)
    ema_top = data[period - 1]
    ema_bottom = 1
    for idx in range(1, period):  # idx 1 to n
        ema_top += ((1 - w)**idx) * data[period - 1 - idx]
        ema_bottom += (1 - w)**idx
    ema = ema_top / ema_bottom
    return ema
