import numpy as np
import catch_errors
from simple_moving_average import simple_moving_average as sma


def upper_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    upper_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        upper_bb.append(simple_ma[idx] + std_dev * std)
    non_computable_values = np.repeat(np.nan, len(data) - len(upper_bb))
    upper_bb = np.append(non_computable_values, upper_bb)

    return np.array(upper_bb)


def middle_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    middle_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        middle_bb.append(simple_ma[idx])
    non_computable_values = np.repeat(np.nan, len(data) - len(middle_bb))
    middle_bb = np.append(non_computable_values, middle_bb)

    return np.array(middle_bb)


def lower_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    lower_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        lower_bb.append(simple_ma[idx] - std_dev * std)
    non_computable_values = np.repeat(np.nan, len(data) - len(lower_bb))
    lower_bb = np.append(non_computable_values, lower_bb)

    return np.array(lower_bb)


def bandwidth(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    bandwidth = (upper_bollinger_band(data, period, std) - lower_bollinger_band(data, period, std)) / middle_bollinger_band(data, period, std)

    return bandwidth


def bb_range(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    bb_range = upper_bollinger_band(data, period, std) - lower_bollinger_band(data, period, std)

    return bb_range


def percent_bandwidth(data, period, std=2.0):
    catch_errors.check_for_period_error

    period = int(period)
    percent_bandwidth = (np.array(data) - lower_bollinger_band(data, period, std)) / bb_range(data, period, std)

    return percent_bandwidth
