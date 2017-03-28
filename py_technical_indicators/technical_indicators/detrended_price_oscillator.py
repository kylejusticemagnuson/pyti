import numpy as np
import catch_errors
from simple_moving_average import simple_moving_average as sma


def detrended_price_oscillator(data, period):
    """
    Detrended Price Oscillator.
    DPO = DATA[i] - Avg(DATA[period/2 + 1])
    """
    period = int(period)
    dop = map(
        lambda idx:
        data[idx] - np.mean(data[idx+1-((period/2)+1):idx+1]),
        range(period-1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(dop))
    dop = np.append(non_computable_values, dop)
    return dop
