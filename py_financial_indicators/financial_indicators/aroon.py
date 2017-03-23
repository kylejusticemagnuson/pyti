import numpy as np
import catch_errors


def aroon_up(data, period):
    """
    Aroon Up.
    AROONUP = (((PERIOD) - (PERIODS since PERIOD high)) / (PERIOD)) * 100
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)
    
    aroon_up = map(
        lambda idx:
        ((period - data[idx+1-period:idx+1].index(np.max(data[idx+1-period:idx+1]))) / period) * 100,
        range(period-1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(aroon_up))
    aroon_up = np.append(non_computable_values, aroon_up)
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
        ((period - data[idx+1-period:idx+1].index(np.min(data[idx+1-period:idx+1]))) / period) * 100,
        range(period-1, len(data)))
    non_computable_values = np.repeat(np.nan, len(data) - len(aroon_down))
    aroon_down = np.append(non_computable_values, aroon_down)
    return aroon_down
