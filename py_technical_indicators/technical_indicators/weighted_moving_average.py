import numpy as np
import catch_errors


def weighted_moving_average(data, period):
    """
    Weighted Moving Average

    Formula:
    (P1 + 2 P2 + 3 P3 + ... + n Pn) / K
    where K = (1+2+...+n) = n(n+1)/2 and Pn is the most recent price
    """
    catch_errors.check_for_period_error(data, period)
    k = (period * (period + 1)) / 2.0

    wmas = []
    for idx in range(0, len(data)-period+1):
        product = map(
            lambda period_idx: data[idx + period_idx] * (period_idx + 1),
            range(0, period)
            )
        wma = sum(product) / k
        wmas.append(wma)
    non_computable_values = np.repeat(np.nan, len(data) - len(wmas))
    wmas = np.append(non_computable_values, wmas)

    return wmas
