from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def standard_deviation(data, period):
    """
    Standard Deviation.

    Formula:
    std = sqrt(avg(abs(x - avg(x))^2))
    """
    catch_errors.check_for_period_error(data, period)

    stds = [np.std(data[idx+1-period:idx+1], ddof=1) for idx in range(period-1, len(data))]

    stds = fill_for_noncomputable_vals(data, stds)
    return stds
