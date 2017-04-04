from py_ti import catch_errors
from py_ti.simple_moving_average import (
    simple_moving_average as sma
    )


def triangular_moving_average(data, period):
    """
    Triangular Moving Average.
    TMA = SMA(SMA())
    """
    catch_errors.check_for_period_error(data, period)

    tma = sma(sma(data, period), period)
    return tma
