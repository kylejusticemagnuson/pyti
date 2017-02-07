import numpy as np

from financial_indicators import catch_errors


def sma(data, period):
    """
    Simple Moving Average.

    Formula: SUM(data / N)
    """
    catch_errors.check_for_period_error(data, period)
    smas = map(lambda idx: np.mean(data[idx-period:idx]), data)
    return smas
