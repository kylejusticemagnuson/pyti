import numpy as np
from pyti import catch_errors
from pyti.function_helper import first_computable_index


def exponential_moving_average(data, period):
    """
    Exponential Moving Average.

    Formula:
    EMAt = alpha * Pt + (1 - alpha) * EMAt-1

    where: alpha = 2 / (N + 1) and the series is seeded with the simple
    moving average of the first N values. Leading NaNs in the input (e.g.
    from a previous indicator's warm-up window) are skipped and preserved
    in the output.
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)
    data = np.asarray(data, dtype=float)
    alpha = 2 / float(period + 1)

    emas = np.full(len(data), np.nan)
    start = first_computable_index(data)
    seed_idx = start + period - 1
    if seed_idx >= len(data):
        return emas
    emas[seed_idx] = np.mean(data[start:seed_idx + 1])
    for idx in range(seed_idx + 1, len(data)):
        emas[idx] = alpha * data[idx] + (1 - alpha) * emas[idx - 1]
    return emas
