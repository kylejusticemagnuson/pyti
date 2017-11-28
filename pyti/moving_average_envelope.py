from __future__ import absolute_import
from pyti.simple_moving_average import simple_moving_average as sma


def center_band(data, period):
    """
    Center Band.

    Formula:
    SMA(data)
    """
    cb = sma(data, period)
    return cb


def upper_band(data, period, env_percentage):
    """
    Upper Band.

    Formula:
    ub = cb(t) * (1 + env_percentage)
    """
    cb = center_band(data, period)
    ub = [val * (1 + float(env_percentage)) for val in cb]
    return ub


def lower_band(data, period, env_percentage):
    """
    Lower Band.

    Formula:
    lb = cb * (1 - env_percentage)
    """
    cb = center_band(data, period)
    lb = [val * (1 - float(env_percentage)) for val in cb]
    return lb
