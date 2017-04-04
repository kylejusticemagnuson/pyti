import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals


def standard_variance(data, period):
    """
    Standard Variance.

    Formula:
    (Ct - AVGt)^2 / N
    """
    catch_errors.check_for_period_error(data, period)
    sv = map(
        lambda idx:
        np.var(data[idx+1-period:idx+1], ddof=1),
        range(period-1, len(data))
        )
    sv = fill_for_noncomputable_vals(data, sv)

    return sv
