from __future__ import absolute_import
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range
from six.moves import zip


def relative_strength_index(data, period):
    """
    Relative Strength Index.

    Formula:
    RSI = 100 - (100 / 1 + (prevGain/prevLoss))
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    changes = [data_tup[1] - data_tup[0] for data_tup in zip(data[::1], data[1::1])]

    gains = [0 if val < 0 else val for val in changes]

    losses = [0 if val > 0 else abs(val) for val in changes]

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    rsi = []
    if avg_loss == 0:
        rsi.append(100)
    else:
        rs = avg_gain / avg_loss
        rsi.append(100 - (100 / (1 + rs)))

    for idx in range(1, len(data) - period):
        avg_gain = ((avg_gain * (period - 1) +
                    gains[idx + (period - 1)]) / period)
        avg_loss = ((avg_loss * (period - 1) +
                    losses[idx + (period - 1)]) / period)

        if avg_loss == 0:
            rsi.append(100)
        else:
            rs = avg_gain / avg_loss
            rsi.append(100 - (100 / (1 + rs)))

    rsi = fill_for_noncomputable_vals(data, rsi)

    return rsi
