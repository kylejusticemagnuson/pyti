from pyti.true_range import true_range
from pyti.smoothed_moving_average import smoothed_moving_average


def average_true_range(close_data, high_data, low_data, period):
    """
    Average True Range.

    Formula:
    ATRt = (ATRt-1 * (n - 1) + TRt) / n
    seeded with the simple moving average of the first n true ranges
    """
    tr = true_range(close_data, high_data, low_data)
    atr = smoothed_moving_average(tr, period)
    return atr
