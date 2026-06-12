import numpy as np
from pyti import catch_errors


def true_range(close_data, high_data, low_data):
    """
    True Range.

    Formula:
    TRt = MAX(Ht - Lt, ABS(Ht - Ct-1), ABS(Lt - Ct-1))
    with TR0 = H0 - L0
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)

    tr = [high_data[0] - low_data[0]]
    for idx in range(1, len(close_data)):
        tr.append(max(
            high_data[idx] - low_data[idx],
            abs(high_data[idx] - close_data[idx-1]),
            abs(low_data[idx] - close_data[idx-1]),
            ))
    return np.array(tr)
