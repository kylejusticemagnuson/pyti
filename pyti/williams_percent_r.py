from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals

def williams_percent_r(high_data, low_data, close_data, period):
    """
    Williams %R.

    Formula:
    wr = (HighestHigh - close / HighestHigh - LowestLow) * -100
    lookback period typically 14 trading days
    """

    catch_errors.check_for_period_error(close_data, period)
    catch_errors.check_for_period_error(high_data, period)
    catch_errors.check_for_period_error(low_data, period)

    wr = [(-100 * (np.max(high_data[idx+1-period:idx+1]) - close_data[idx] ) / 
           (np.max(high_data[idx+1-period:idx+1]) - 
            np.min(low_data[idx+1-period:idx+1]))) for idx in range(period-1, len(close_data))]
    wr = fill_for_noncomputable_vals(close_data, wr)

    return wr
