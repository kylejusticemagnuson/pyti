from py_ti.standard_deviation import standard_deviation as sd
from py_ti.standard_variance import standard_variance as sv


def volatility(data, period):
    """
    Volatility.
    SDt / SVt
    """
    volatility = sd(data, period) / sv(data, period)
    return volatility
