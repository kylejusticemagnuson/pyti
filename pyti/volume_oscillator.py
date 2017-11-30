from __future__ import absolute_import
from pyti import catch_errors
from pyti.simple_moving_average import simple_moving_average as sma


def volume_oscillator(volume, short_period, long_period):
    """
    Volume Oscillator.

    Formula:
    vo = 100 * (SMA(vol, short) - SMA(vol, long) / SMA(vol, long))
    """
    catch_errors.check_for_period_error(volume, short_period)
    catch_errors.check_for_period_error(volume, long_period)

    vo = (100 * ((sma(volume, short_period) - sma(volume, long_period)) /
          sma(volume, long_period)))
    return vo
