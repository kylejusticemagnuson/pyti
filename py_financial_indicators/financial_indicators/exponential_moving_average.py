import numpy as np
from financial_indicators import catch_errors


def exponential_moving_average(data, period):
    """
    Exponential Moving Average.

    Formula: p0 + (1 - w) * p1 + (1 - w)^2 * p2 + (1 + w)^3 * p3 +...
                /   1 + (1 - w) + (1 - w)^2 + (1 - w)^3 +...

            where: w = 2 / (N + 1)
    """
    catch_errors.check_for_period_error(data, period)
    exponential_moving_averages = map(
        lambda idx:
        exponential_moving_average_helper(data[idx - period + 1:idx + 1], period),
        range(period - 1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(exponential_moving_averages))
    exponential_moving_averages = np.append(non_computable_values, exponential_moving_averages)
    return exponential_moving_averages


def exponential_moving_average_helper(data, period):
    w = 2 / float(period + 1)
    exponential_moving_average_top = data[period - 1]
    exponential_moving_average_bottom = 1
    for idx in range(1, period):  # idx 1 to n
        exponential_moving_average_top += ((1 - w)**idx) * data[period - 1 - idx]
        exponential_moving_average_bottom += (1 - w)**idx
    exponential_moving_average = exponential_moving_average_top / exponential_moving_average_bottom
    return exponential_moving_average
