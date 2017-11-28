from __future__ import absolute_import
from pyti import catch_errors
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def price_oscillator(data, short_period, long_period):
    """
    Price Oscillator.

    Formula:
    (short EMA - long EMA / long EMA) * 100
    """
    catch_errors.check_for_period_error(data, short_period)
    catch_errors.check_for_period_error(data, long_period)

    ema_short = ema(data, short_period)
    ema_long = ema(data, long_period)

    po = ((ema_short - ema_long) / ema_long) * 100
    return po
