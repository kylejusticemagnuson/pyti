from __future__ import absolute_import
import numpy as np
from pyti.true_range import true_range
from pyti.smoothed_moving_average import smoothed_moving_average
from six.moves import range


def average_true_range(close_data, period):
    """
    Average True Range.

    Formula:
    ATRt = ATRt-1 * (n - 1) + TRt / n
    """
    tr = true_range(close_data, period)
    atr = smoothed_moving_average(tr, period)
    atr[0:period-1] = tr[0:period-1]
    return atr
