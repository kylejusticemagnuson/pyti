import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals


def detrended_price_oscillator(data, period):
    """
    Detrended Price Oscillator.

    Formula:
    DPO[i] = DATA[i] - SMA(period)[i - (period/2 + 1)]
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)
    shift = period // 2 + 1
    dop = [data[idx] - np.mean(data[idx+1-shift-period:idx+1-shift]) for idx in range(period+shift-1, len(data))]
    dop = fill_for_noncomputable_vals(data, dop)
    return dop
