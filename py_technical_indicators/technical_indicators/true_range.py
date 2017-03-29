import numpy as np
import catch_errors


def true_range(close_data, period):
    """
    True Range.
    TRt = MAX(abs(Ht - Lt), abs(Ht - Ct-1), abs(Lt - Ct-1))
    """
    catch_errors.check_for_period_error(close_data, period)

    tr = map(
        lambda idx:
        np.max([np.max(close_data[idx+1-period:idx+1]) - np.min(close_data[idx+1-period:idx+1]), abs(np.max(close_data[idx+1-period:idx+1]) - close_data[idx-1]), abs(np.min(close_data[idx+1-period:idx+1]) - close_data[idx-1])]),
        range(period-1, len(close_data))
        )
    non_computable_values = np.repeat(np.nan, len(close_data) - len(tr))
    tr = np.append(non_computable_values, tr)
    return tr
