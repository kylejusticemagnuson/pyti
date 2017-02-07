import numpy as np


def sma(data, period):
    """
    Simple Moving Average.

    Formula: SUM(data / N)
    """
    smas = map(lambda idx: np.mean(data[idx-period:idx]), data)
    return smas
