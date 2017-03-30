import numpy as np
import warnings

from technical_indicators import catch_errors


def simple_moving_average(data, period):
    """
    Simple Moving Average.

    Formula: SUM(data / N)
    """
    catch_errors.check_for_period_error(data, period)
    # Mean of Empty Slice RuntimeWarning doesn't affect output so it is
    # supressed
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        simple_moving_averages = map(
            lambda idx: np.mean(data[idx-(period-1):idx+1]),
            range(0, len(data))
            )
    non_computable_values = np.repeat(np.nan, len(data) - len(simple_moving_averages))
    simple_moving_averages = np.append(non_computable_values, simple_moving_averages)
    return simple_moving_averages
