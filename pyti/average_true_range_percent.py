from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.average_true_range import (
    average_true_range as atr
    )


def average_true_range_percent(close_data, period):
    """
    Average True Range Percent.

    Formula:
    ATRP = (ATR / CLOSE) * 100
    """
    catch_errors.check_for_period_error(close_data, period)
    atrp = (atr(close_data, period) / np.array(close_data)) * 100
    return atrp
