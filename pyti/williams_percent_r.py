import numpy as np


def williams_percent_r(close_data):
    """
    Williams %R.

    Formula:
    wr = (HighestHigh - close / HighestHigh - LowestLow) * -100
    """
    highest_high = np.max(close_data)
    lowest_low = np.min(close_data)
    wr = map(
        lambda close:
        ((highest_high - close) / (highest_high - lowest_low)) * -100,
        close_data
        )
    return wr
