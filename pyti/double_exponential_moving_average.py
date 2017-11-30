from __future__ import absolute_import
from pyti import catch_errors
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def double_exponential_moving_average(data, period):
    """
    Double Exponential Moving Average.

    Formula:
    DEMA = 2*EMA - EMA(EMA)
    """
    catch_errors.check_for_period_error(data, period)

    dema = (2 * ema(data, period)) - ema(ema(data, period), period)
    return dema
