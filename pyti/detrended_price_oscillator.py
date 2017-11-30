from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def detrended_price_oscillator(data, period):
    """
    Detrended Price Oscillator.

    Formula:
    DPO = DATA[i] - Avg(DATA[period/2 + 1])
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)
    dop = [data[idx] - np.mean(data[idx+1-(int(period/2)+1):idx+1]) for idx in range(period-1, len(data))]
    dop = fill_for_noncomputable_vals(data, dop)
    return dop
