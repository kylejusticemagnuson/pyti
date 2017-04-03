import numpy as np
from py_technical_indicators import catch_errors
from py_technical_indicators.function_helper import fill_for_noncomputable_vals


def smoothed_moving_average(data, period):
    """
    Smoothed Moving Average.
    """
    catch_errors.check_for_period_error(data, period)
    smma = map(
        lambda idx:
        ((np.mean(data[idx-(period-1):idx+1]) -
         (np.mean(data[idx-(period-1):idx+1])/period) +
         data[idx])/period),
        range(0, len(data))
        )
    smma = fill_for_noncomputable_vals(data, smma)
    return smma
