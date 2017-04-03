import numpy as np
import catch_errors


def rate_of_change(data, period):
    """
    Rate of Change

    Formula:
    (Close - Close n periods ago) / (Close n periods ago) * 100
    """
    catch_errors.check_for_period_error(data, period)

    rocs = map(
        lambda idx:
        ((data[idx] - data[idx - (period - 1)]) / data[idx - (period - 1)]) * 100,
        range(period - 1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(rocs))
    rocs = np.append(non_computable_values, rocs)
    return rocs
