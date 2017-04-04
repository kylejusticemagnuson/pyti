import numpy as np
from py_ti import catch_errors
from py_ti.function_helper import fill_for_noncomputable_vals
from py_ti.simple_moving_average import (
    simple_moving_average as sma
    )


def upper_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    upper_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        upper_bb.append(simple_ma[idx] + std_dev * std)
    upper_bb = fill_for_noncomputable_vals(data, upper_bb)

    return np.array(upper_bb)


def middle_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    middle_bb = []
    for idx in range(len(data) - period + 1):
        middle_bb.append(simple_ma[idx])
    middle_bb = fill_for_noncomputable_vals(data, middle_bb)

    return np.array(middle_bb)


def lower_bollinger_band(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    simple_ma = sma(data, period)[period-1:]

    lower_bb = []
    for idx in range(len(data) - period + 1):
        std_dev = np.std(data[idx:idx + period])
        lower_bb.append(simple_ma[idx] - std_dev * std)
    lower_bb = fill_for_noncomputable_vals(data, lower_bb)

    return np.array(lower_bb)


def bandwidth(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    bandwidth = ((upper_bollinger_band(data, period, std) -
                 lower_bollinger_band(data, period, std)) /
                 middle_bollinger_band(data, period, std)
                 )

    return bandwidth


def bb_range(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    bb_range = (upper_bollinger_band(data, period, std) -
                lower_bollinger_band(data, period, std)
                )
    return bb_range


def percent_bandwidth(data, period, std=2.0):
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    percent_bandwidth = ((np.array(data) -
                         lower_bollinger_band(data, period, std)) /
                         bb_range(data, period, std)
                         )

    return percent_bandwidth
