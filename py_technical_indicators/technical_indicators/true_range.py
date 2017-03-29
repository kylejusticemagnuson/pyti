import numpy as np
import catch_errors


def true_range(close_data, high_data, low_data):
    """
    True Range.
    TRt = MAX(abs(Ht - Lt), abs(Ht - Ct), abs(Lt - Ct-1))
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)

    tr = map(lambda idx: np.max([abs(high_data[idx] - low_data[idx]), abs(high_data[idx] - close_data[idx]), abs(low_data[idx] - close_data[idx-1])]), range(1, len(close_data)))
    non_computable_values = np.repeat(np.nan, len(close_data) - len(tr))
    tr = np.append(non_computable_values, tr)
    return tr
