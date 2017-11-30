from __future__ import absolute_import
from pyti import catch_errors
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def upper_price_channel(data, period, upper_percent):
    """
    Upper Price Channel.

    Formula:
    upc = EMA(t) * (1 + upper_percent / 100)
    """
    catch_errors.check_for_period_error(data, period)

    emas = ema(data, period)
    upper_channel = [val * (1+float(upper_percent)/100) for val in emas]
    return upper_channel


def lower_price_channel(data, period, lower_percent):
    """
    Lower Price Channel.

    Formula:
    lpc = EMA(t) * (1 - lower_percent / 100)
    """
    catch_errors.check_for_period_error(data, period)

    emas = ema(data, period)
    lower_channel = [val * (1-float(lower_percent)/100) for val in emas]
    return lower_channel
