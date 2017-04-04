from py_ti import catch_errors
from py_ti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def triple_exponential_moving_average(data, period):
    """
    Triple Exponential Moving Average

    TEMA = (3*EMA - 3*EMA(EMA)) + EMA(EMA(EMA))
    """
    catch_errors.check_for_period_error(data, period)

    tema = ((3 * ema(data, period) - (3 * ema(ema(data, period), period))) +
            ema(ema(ema(data, period), period), period)
            )
    return tema
