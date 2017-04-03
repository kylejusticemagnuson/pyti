import numpy as np
from standard_deviation import standard_deviation as sd
from standard_variance import standard_variance as sv


def volatility(data, period):
    """
    Volatility.
    SDt / SVt
    """
    volatility = sd(data, period) / sv(data, period)
    return volatility
