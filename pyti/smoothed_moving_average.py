from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range

import pandas as pd

def smoothed_moving_average(data, period):
    """
    Smoothed Moving Average.

    Formula:
    smma = avg(data(n)) - avg(data(n)/n) + data(t)/n
    """
    catch_errors.check_for_period_error(data, period)
    series = pd.Series(data)
    return series.ewm(alpha = 1.0/period).mean().values.flatten()
