import numpy as np
from py_ti import catch_errors


def volume_index_helper(vi, idx, close_data, volume):
    return (vi[idx-1] + (((close_data[idx] - close_data[idx-1]) /
            close_data[idx-1]) * vi[idx-1])
            )


def positive_volume_index(close_data, volume):
    """
    Positive Volume Index (PVI)
    PVI0 = 1
    IF Vt > Vt-1
        PVIt = PVIt-1 + (CLOSEt - CLOSEt-1 / CLOSEt-1 * PVIt-1)
    ELSE:
        PVIt = PVIt-1
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    pvi = np.zeros(len(volume))
    pvi[0] = 1
    for idx in range(1, len(volume)):
        if volume[idx] > volume[idx-1]:
            pvi[idx] = volume_index_helper(pvi, idx, close_data, volume)
        else:
            pvi[idx] = pvi[idx-1]
    return pvi


def negative_volume_index(close_data, volume):
    """
    Negative Volume Index (NVI)
    NVI0 = 1
    IF Vt < Vt-1
        NVIt = NVIt-1 + (CLOSEt - CLOSEt-1 / CLOSEt-1 * NVIt-1)
    ELSE:
        NVIt = NVIt-1
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    nvi = np.zeros(len(volume))
    nvi[0] = 1
    for idx in range(1, len(volume)):
        if volume[idx] < volume[idx-1]:
            nvi[idx] = volume_index_helper(nvi, idx, close_data, volume)
        else:
            nvi[idx] = nvi[idx-1]
    return nvi
