import numpy as np
import catch_errors


def smoothed_moving_average(data, period):
    """
    Smoothed Moving Average.
    """
    catch_errors.check_for_period_error(data, period)
    smma = map(
        lambda idx:
        ((np.mean(data[idx-(period-1):idx+1])/period) - ((np.mean(data[idx-(period-1):idx+1])/period)/period) + data[idx])/period,
        range(0, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(smma))
    smma = np.append(non_computable_values, smma)
    return smma
