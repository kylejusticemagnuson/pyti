import numpy as np
from py_technical_indicators import catch_errors


def typical_price(close_data, high_data, low_data):
    """
    Typical Price.
    TPt = (HIGHt + LOWt + CLOSEt) / 3
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    tp = map(
        lambda idx:
        (high_data[idx] + low_data[idx] + close_data[idx]) / 3,
        range(0, len(close_data))
        )
    return np.array(tp)
