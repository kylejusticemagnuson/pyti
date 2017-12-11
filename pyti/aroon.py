from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def aroon_up(data, period):
    """
    Aroon Up.

    Formula:
    AROONUP = (((PERIOD) - (PERIODS since PERIOD high)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)

    a_up = [((period -
            list(reversed(data[idx+1-period:idx+1])).index(np.max(data[idx+1-period:idx+1]))) /
            float(period)) * 100 for idx in range(period-1, len(data))]
    a_up = fill_for_noncomputable_vals(data, a_up)
    return a_up


def aroon_down(data, period):
    """
    Aroon Down.

    Formula:
    AROONDWN = (((PERIOD) - (PERIODS SINCE PERIOD LOW)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)

    a_down = [((period -
            list(reversed(data[idx+1-period:idx+1])).index(np.min(data[idx+1-period:idx+1]))) /
            float(period)) * 100 for idx in range(period-1, len(data))]
    a_down = fill_for_noncomputable_vals(data, a_down)
    return a_down
