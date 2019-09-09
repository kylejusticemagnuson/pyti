from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def true_strength_index(close_data):
    """
    True Strength Index.

    Double Smoothed PC
    ------------------
    PC = Current Price minus Prior Price
    First Smoothing = 25-period EMA of PC
    Second Smoothing = 13-period EMA of 25-period EMA of PC

    Double Smoothed Absolute PC
    ---------------------------
    Absolute Price Change |PC| = Absolute Value of Current Price minus Prior Price
    First Smoothing = 25-period EMA of |PC|
    Second Smoothing = 13-period EMA of 25-period EMA of |PC|

    TSI = 100 x (Double Smoothed PC / Double Smoothed Absolute PC)
    """
    if len(close_data) < 40:
        raise RuntimeError("Data must have at least 40 items")

    pc = np.diff(close_data, 1)
    apc = np.abs(pc)

    num = ema(pc, 25)
    num = ema(num, 13)
    den = ema(apc, 25)
    den = ema(den, 13)

    tsi = 100 * num / den
    tsi = fill_for_noncomputable_vals(close_data, tsi)
    return tsi