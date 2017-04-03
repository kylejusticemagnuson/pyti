import numpy as np
import warnings
from py_technical_indicators import catch_errors


def chande_momentum_oscillator(close_data, period):
    """
    Chande Momentum Oscillator.
    """
    catch_errors.check_for_period_error(close_data, period)

    close_data = np.array(close_data)

    moving_period_diffs = map(
        lambda idx:
            map(lambda i:
                (close_data[idx+1-period:idx+1][i] -
                 close_data[idx+1-period:idx+1][i-1]),
                range(1, len(close_data[idx+1-period:idx+1]))),
            range(0, len(close_data))
        )

    sum_up = []
    sum_down = []
    for period_diffs in moving_period_diffs:
        ups = map(lambda val: val if val > 0 else 0, period_diffs)
        sum_up.append(sum(ups))
        downs = map(lambda val: abs(val) if val < 0 else 0, period_diffs)
        sum_down.append(sum(downs))

    sum_up = np.array(sum_up)
    sum_down = np.array(sum_down)
    # numpy is able to handle dividing by zero and makes those calculations
    # nans which is what we want, so we safely suppress the RuntimeWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        cmo = 100 * ((sum_up - sum_down) / (sum_up + sum_down))
    return cmo
