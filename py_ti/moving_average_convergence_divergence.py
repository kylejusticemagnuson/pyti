from py_ti import catch_errors
from py_ti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def moving_average_convergence_divergence(data, short_period, long_period):
    """
    Moving Average Convergence Divergence.
    EMA(DATA, P1) - EMA(DATA, P2)
    """
    catch_errors.check_for_period_error(data, short_period)
    catch_errors.check_for_period_error(data, long_period)

    macd = ema(data, short_period) - ema(data, long_period)
    return macd
