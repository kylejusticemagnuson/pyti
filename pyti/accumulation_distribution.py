from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from six.moves import range


def accumulation_distribution(close_data, high_data, low_data, volume):
    """
    Accumulation/Distribution.

    Formula:
    A/D = (Ct - Lt) - (Ht - Ct) / (Ht - Lt) * Vt + A/Dt-1
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume
        )

    ad = np.zeros(len(close_data))
    for idx in range(1, len(close_data)):
        ad[idx] = (
            (((close_data[idx] - low_data[idx]) -
                (high_data[idx] - close_data[idx])) /
                (high_data[idx] - low_data[idx]) *
                volume[idx]) +
            ad[idx-1]
            )
    return ad
