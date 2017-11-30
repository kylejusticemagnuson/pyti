from __future__ import absolute_import
from pyti import catch_errors
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def triple_exponential_moving_average(data, period):
    """
    Triple Exponential Moving Average.

    Formula:
    TEMA = (3*EMA - 3*EMA(EMA)) + EMA(EMA(EMA))
    """
    catch_errors.check_for_period_error(data, period)

    tema = ((3 * ema(data, period) - (3 * ema(ema(data, period), period))) +
            ema(ema(ema(data, period), period), period)
            )
    return tema
