import numpy as np
import catch_errors


def standard_deviation(data, period):
    """
    Standard Deviation
    """
    catch_errors.check_for_period_error(data, period)

    lookback_period = int(period)
    standard_deviations = map(
        lambda idx: np.std(data[idx+1-period:idx+1], ddof=1),
        range(period-1, len(data)))

    non_computable_values = np.repeat(np.nan, len(data) - len(standard_deviations))
    standard_deviations = np.append(non_computable_values, standard_deviations)
    return standard_deviations
