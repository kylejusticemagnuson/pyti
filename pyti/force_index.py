from __future__ import absolute_import
from pyti import catch_errors
import numpy as np


def force_index(close_data, volume):
    """
    Force Index.

    Formula:
    """
    catch_errors.check_for_input_len_diff(
        close_data, volume
        )

    pc = np.diff(close_data, 1)
    fi = pc * volume[1:]
    fi = np.append(np.nan, fi)
    return fi