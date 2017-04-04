import numpy as np
from py_ti import catch_errors
from py_ti.weighted_moving_average import (
    weighted_moving_average as wma
    )


def hull_moving_average(data, period):
    """
    Hull Moving Average.
    HMA = WMA(2*WMA(n/2) - WMA(n)), sqrt(n)
    """
    catch_errors.check_for_period_error(data, period)
    hma = wma(
        2 * wma(data, int(period/2)) - wma(data, period), int(np.sqrt(period))
        )
    return hma
