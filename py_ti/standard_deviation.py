import numpy as np
from py_ti import catch_errors
from py_ti.function_helper import fill_for_noncomputable_vals


def standard_deviation(data, period):
    """
    Standard Deviation
    """
    catch_errors.check_for_period_error(data, period)

    stds = map(
        lambda idx:
        np.std(data[idx+1-period:idx+1], ddof=1),
        range(period-1, len(data))
        )

    stds = fill_for_noncomputable_vals(data, stds)
    return stds
