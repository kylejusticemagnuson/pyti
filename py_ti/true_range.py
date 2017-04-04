import numpy as np
from py_ti import catch_errors
from py_ti.function_helper import fill_for_noncomputable_vals


def true_range(close_data, period):
    """
    True Range.
    TRt = MAX(abs(Ht - Lt), abs(Ht - Ct-1), abs(Lt - Ct-1))
    """
    catch_errors.check_for_period_error(close_data, period)

    tr = map(
        lambda idx:
        np.max([np.max(close_data[idx+1-period:idx+1]) -
                np.min(close_data[idx+1-period:idx+1]),
                abs(np.max(close_data[idx+1-period:idx+1]) -
                close_data[idx-1]),
                abs(np.min(close_data[idx+1-period:idx+1]) -
                close_data[idx-1])]),
        range(period-1, len(close_data))
        )
    tr = fill_for_noncomputable_vals(close_data, tr)
    return tr
