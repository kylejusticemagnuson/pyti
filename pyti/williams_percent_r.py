import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals


def williams_percent_r(close_data, high_data, low_data, period):
    """
    Williams %R.

    Formula:
    %R = (HighestHigh(n) - Ct) / (HighestHigh(n) - LowestLow(n)) * -100
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    catch_errors.check_for_period_error(close_data, period)

    wr = [((np.max(high_data[idx+1-period:idx+1]) - close_data[idx]) /
           (np.max(high_data[idx+1-period:idx+1]) -
            np.min(low_data[idx+1-period:idx+1]))) * -100
          for idx in range(period-1, len(close_data))]
    wr = fill_for_noncomputable_vals(close_data, wr)
    return wr
