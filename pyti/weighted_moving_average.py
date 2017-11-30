from __future__ import absolute_import
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def weighted_moving_average(data, period):
    """
    Weighted Moving Average.

    Formula:
    (P1 + 2 P2 + 3 P3 + ... + n Pn) / K
    where K = (1+2+...+n) = n(n+1)/2 and Pn is the most recent price
    """
    catch_errors.check_for_period_error(data, period)
    k = (period * (period + 1)) / 2.0

    wmas = []
    for idx in range(0, len(data)-period+1):
        product = [data[idx + period_idx] * (period_idx + 1) for period_idx in range(0, period)]
        wma = sum(product) / k
        wmas.append(wma)
    wmas = fill_for_noncomputable_vals(data, wmas)

    return wmas
