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

    aroon_up = [((period -
            data[idx+1-period:idx+1].index(np.max(data[idx+1-period:idx+1]))) /
            period) * 100 for idx in range(period-1, len(data))]
    aroon_up = fill_for_noncomputable_vals(data, aroon_up)
    return aroon_up


def aroon_down(data, period):
    """
    Aroon Down.

    Formula:
    AROONDWN = (((PERIOD) - (PERIODS SINCE PERIOD LOW)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)

    aroon_down = [((period -
            data[idx+1-period:idx+1].index(np.min(data[idx+1-period:idx+1]))) /
            period) * 100 for idx in range(period-1, len(data))]
    aroon_down = fill_for_noncomputable_vals(data, aroon_down)
    return aroon_down
