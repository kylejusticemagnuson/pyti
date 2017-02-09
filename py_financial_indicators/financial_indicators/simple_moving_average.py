import numpy as np

from financial_indicators import catch_errors


def sma(data, period):
    """
    Simple Moving Average.

    Formula: SUM(data / N)
    """
    catch_errors.check_for_period_error(data, period)
    smas = map(
        lambda idx: np.mean(data[idx-(period-1):idx+1]),
        range(0, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(smas))
    smas = np.append(non_computable_values, smas)
    return smas
