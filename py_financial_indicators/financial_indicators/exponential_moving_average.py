import numpy as np


def ema(data, period):
    """
    Exponential Moving Average.

    Moving average where more weight is given to recent values.
    """
    period = int(period)
    data_len = len(data)
    if data_len < period:
        # show error message
        raise SystemExit('Error: data_len < period')
    emas = map(
        lambda idx:
        ema_helper(data[idx - period + 1:idx + 1], period),
        range(period - 1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(emas))
    emas = np.append(non_computable_values, emas)
    return emas


def ema_helper(data, period):
    w = 2 / float(period + 1)
    ema_top = data[period - 1]
    ema_bottom = 1
    for idx in range(1, period):  # idx 1 to n
        ema_top += ((1 - w)**idx) * data[period - 1 - idx]
        ema_bottom += (1 - w)**idx
    ema = ema_top / ema_bottom
    return ema
