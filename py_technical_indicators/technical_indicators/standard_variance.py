import numpy as np
import catch_errors
from simple_moving_average import simple_moving_average as sma


def standard_variance(data, period):
    """
    Standard Variance.

    (Ct - AVGt)^2 / N
    """
    sv = map(
        lambda idx:
        np.var(data[idx+1-period:idx+1], ddof=1),
        range(period-1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(sv))
    sv = np.append(non_computable_values, sv)

    return sv
