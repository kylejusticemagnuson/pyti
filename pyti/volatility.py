from __future__ import absolute_import
from pyti.standard_deviation import standard_deviation as sd
from pyti.standard_variance import standard_variance as sv


def volatility(data, period):
    """
    Volatility.

    Formula:
    SDt / SVt
    """
    volatility = sd(data, period) / sv(data, period)
    return volatility
