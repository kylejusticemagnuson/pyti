from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def vertical_horizontal_filter(data, period):
    """
    Vertical Horizontal Filter.

    Formula:
    ABS(pHIGH - pLOW) / SUM(ABS(Pi - Pi-1))
    """
    catch_errors.check_for_period_error(data, period)

    vhf = [abs(np.max(data[idx+1-period:idx+1]) -
            np.min(data[idx+1-period:idx+1])) /
        sum([abs(data[idx+1-period:idx+1][i] - data[idx+1-period:idx+1][i-1]) for i in range(0, len(data[idx+1-period:idx+1]))]) for idx in range(period - 1, len(data))]

    vhf = fill_for_noncomputable_vals(data, vhf)
    return vhf
