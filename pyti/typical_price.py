from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from six.moves import range


def typical_price(close_data, high_data, low_data):
    """
    Typical Price.

    Formula:
    TPt = (HIGHt + LOWt + CLOSEt) / 3
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    tp = [(high_data[idx] + low_data[idx] + close_data[idx]) / 3 for idx in range(0, len(close_data))]
    return np.array(tp)
