from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from six.moves import range


def on_balance_volume(close_data, volume):
    """
    On Balance Volume.

    Formula:
    start = 1
    if CLOSEt > CLOSEt-1
        obv = obvt-1 + volumet
    elif CLOSEt < CLOSEt-1
        obv = obvt-1 - volumet
    elif CLOSEt == CLOSTt-1
        obv = obvt-1
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    obv = np.zeros(len(volume))
    obv[0] = 1
    for idx in range(1, len(obv)):
        if close_data[idx] > close_data[idx-1]:
            obv[idx] = obv[idx-1] + volume[idx]
        elif close_data[idx] < close_data[idx-1]:
            obv[idx] = obv[idx-1] - volume[idx]
        elif close_data[idx] == close_data[idx-1]:
            obv[idx] = obv[idx-1]
    return obv
