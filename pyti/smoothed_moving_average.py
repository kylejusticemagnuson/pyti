import numpy as np
from pyti import catch_errors
from pyti.function_helper import first_computable_index


def smoothed_moving_average(data, period):
    """
    Smoothed Moving Average (Wilder's Moving Average).

    Formula:
    SMMAt = (SMMAt-1 * (N - 1) + Pt) / N

    seeded with the simple moving average of the first N values. Leading
    NaNs in the input (e.g. from a previous indicator's warm-up window)
    are skipped and preserved in the output.
    """
    catch_errors.check_for_period_error(data, period)
    period = int(period)
    data = np.asarray(data, dtype=float)

    smma = np.full(len(data), np.nan)
    start = first_computable_index(data)
    seed_idx = start + period - 1
    if seed_idx >= len(data):
        return smma
    smma[seed_idx] = np.mean(data[start:seed_idx + 1])
    for idx in range(seed_idx + 1, len(data)):
        smma[idx] = (smma[idx - 1] * (period - 1) + data[idx]) / period
    return smma
