import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals


def volume_adjusted_moving_average(close_data, volume, period):
    """
    Volume Adjusted Moving Average.

    Formula:
    VAMA = SUM(CLOSE * VolumeRatio) / period
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    catch_errors.check_for_period_error(close_data, period)

    avg_vol = np.mean(volume)
    vol_incr = avg_vol * 0.67
    vol_ratio = map(lambda val: val / vol_incr, volume)
    close_vol = np.array(close_data) * vol_ratio
    vama = map(
        lambda idx:
        sum(close_vol[idx+1-period:idx+1]) / period,
        range(period-1, len(close_data))
        )
    vama = fill_for_noncomputable_vals(close_data, vama)
    return vama
