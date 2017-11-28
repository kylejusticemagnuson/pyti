from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.weighted_moving_average import (
    weighted_moving_average as wma
    )


def hull_moving_average(data, period):
    """
    Hull Moving Average.

    Formula:
    HMA = WMA(2*WMA(n/2) - WMA(n)), sqrt(n)
    """
    catch_errors.check_for_period_error(data, period)
    hma = wma(
        2 * wma(data, int(period/2)) - wma(data, period), int(np.sqrt(period))
        )
    return hma
