import numpy as np
import catch_errors


def calculate_up_moves(high_data):
    up_moves = map(lambda idx: high_data[idx] - high_data[idx-1], range(1, len(high_data)))
    return [np.nan] + up_moves


def calculate_down_moves(low_data):
    down_moves = map(lambda idx: low_data[idx] - low_data[idx-1], range(1, len(low_data)))
    return [np.nan] + down_moves


def positive_directional_movement(high_data, low_data):
    """
    Positive Directional Movement (+DM)
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
    Negative Directional Movement (-DM)
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
