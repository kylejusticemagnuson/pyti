import numpy as np
from py_technical_indicators import catch_errors
from py_technical_indicators.function_helper import fill_for_noncomputable_vals


def aroon_up(data, period):
    """
    Aroon Up.
    AROONUP = (((PERIOD) - (PERIODS since PERIOD high)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)

    aroon_up = map(
        lambda idx:
        ((period -
            data[idx+1-period:idx+1].index(np.max(data[idx+1-period:idx+1]))) /
            period) * 100,
        range(period-1, len(data))
        )
    aroon_up = fill_for_noncomputable_vals(data, aroon_up)
    return aroon_up


def aroon_down(data, period):
    """
    Aroon Down.
    AROONDWN = (((PERIOD) - (PERIODS SINCE PERIOD LOW)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)

    aroon_down = map(
        lambda idx:
        ((period -
            data[idx+1-period:idx+1].index(np.min(data[idx+1-period:idx+1]))) /
            period) * 100,
        range(period-1, len(data)))
    aroon_down = fill_for_noncomputable_vals(data, aroon_down)
    return aroon_down
