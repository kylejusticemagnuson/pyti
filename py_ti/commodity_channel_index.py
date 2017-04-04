import numpy as np
from py_ti import catch_errors
from py_ti.typical_price import typical_price
from py_ti.simple_moving_average import (
    simple_moving_average as sma
    )


def commodity_channel_index(close_data, high_data, low_data, period):
    """
    Commodity Channel Index.
    CCI = (TP - SMA(TP)) / (0.015 * Mean Deviation)
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    catch_errors.check_for_period_error(close_data, period)
    tp = typical_price(close_data, high_data, low_data)
    cci = ((tp - sma(tp, period)) /
           (0.015 * np.mean(np.absolute(tp - np.mean(tp)))))
    return cci
