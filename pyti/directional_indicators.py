from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.smoothed_moving_average import (
    smoothed_moving_average as smma
    )
from pyti.average_true_range import (
    average_true_range as atr
    )
from six.moves import range


def calculate_up_moves(high_data):
    """
    Up Move.

    Formula:
    UPMOVE = Ht - Ht-1
    """
    up_moves = [high_data[idx] - high_data[idx-1] for idx in range(1, len(high_data))]
    return [np.nan] + up_moves


def calculate_down_moves(low_data):
    """
    Down Move.

    Formula:
    DWNMOVE = Lt-1 - Lt
    """
    down_moves = [low_data[idx-1] - low_data[idx] for idx in range(1, len(low_data))]
    return [np.nan] + down_moves


def positive_directional_movement(high_data, low_data):
    """
    Positive Directional Movement (+DM).

    Formula:
    +DM: if UPMOVE > DWNMOVE and UPMOVE > 0 then +DM = UPMOVE else +DM = 0
    """
    catch_errors.check_for_input_len_diff(high_data, low_data)
    up_moves = calculate_up_moves(high_data)
    down_moves = calculate_down_moves(low_data)

    pdm = []
    for idx in range(0, len(up_moves)):
        if up_moves[idx] > down_moves[idx] and up_moves[idx] > 0:
            pdm.append(up_moves[idx])
        else:
            pdm.append(0)

    return pdm


def negative_directional_movement(high_data, low_data):
    """
    Negative Directional Movement (-DM).


    -DM: if DWNMOVE > UPMOVE and DWNMOVE > 0 then -DM = DWNMOVE else -Dm = 0
    """
    catch_errors.check_for_input_len_diff(high_data, low_data)
    up_moves = calculate_up_moves(high_data)
    down_moves = calculate_down_moves(low_data)

    ndm = []
    for idx in range(0, len(down_moves)):
        if down_moves[idx] > up_moves[idx] and down_moves[idx] > 0:
            ndm.append(down_moves[idx])
        else:
            ndm.append(0)

    return ndm


def positive_directional_index(close_data, high_data, low_data, period):
    """
    Positive Directional Index (+DI).

    Formula:
    +DI = 100 * SMMA(+DM) / ATR
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    pdi = (100 *
           smma(positive_directional_movement(high_data, low_data), period) /
           atr(close_data, period)
           )
    return pdi


def negative_directional_index(close_data, high_data, low_data, period):
    """
    Negative Directional Index (-DI).

    Formula:
    -DI = 100 * SMMA(-DM) / ATR
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    ndi = (100 *
           smma(negative_directional_movement(high_data, low_data), period) /
           atr(close_data, period)
           )
    return ndi


def average_directional_index(close_data, high_data, low_data, period):
    """
    Average Directional Index.

    Formula:
    ADX = 100 * SMMA(abs((+DI - -DI) / (+DI + -DI)))
    """
    avg_di = (abs(
              (positive_directional_index(
                close_data, high_data, low_data, period) -
              negative_directional_index(
                close_data, high_data, low_data, period)) /
              (positive_directional_index(
                close_data, high_data, low_data, period) +
               negative_directional_index(
                close_data, high_data, low_data, period)))
              )
    adx = 100 * smma(avg_di, period)
    return adx
