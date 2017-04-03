import numpy as np
from py_technical_indicators.true_range import true_range


def average_true_range(close_data, period):
    """
    Average True Range.
    ATRt = ATRt-1 * (n - 1) + TRt / n
    """
    tr = true_range(close_data, period)
    atr = np.zeros(len(tr))
    atr[0:period-1] = tr[0:period-1]
    atr[period-1:period-1+period-1] = tr[0:period-1]
    atr[period-1+period-1] = ((1 / float(period)) *
                              sum(tr[period-1:period-1+period])
                              )
    for idx in range(period-1+period, len(tr)):
        atr[idx] = (atr[idx-1] * (period - 1) + tr[idx]) / period
    return atr
