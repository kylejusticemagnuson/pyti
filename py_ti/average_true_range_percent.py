import numpy as np
from py_ti import catch_errors
from py_ti.average_true_range import (
    average_true_range as atr
    )


def average_true_range_percent(close_data, period):
    """
    Average True Range Percent.
    ATRP = (ATR / CLOSE) * 100
    """
    catch_errors.check_for_period_error(close_data, period)
    atrp = (atr(close_data, period) / np.array(close_data)) * 100
    return atrp
