import numpy as np
import catch_errors
from exponential_moving_average import exponential_moving_average as ema


def moving_average_convergence_divergence(data, period_1, period_2):
    """
    Moving Average Convergence Divergence.
    EMA(DATA, P1) - EMA(DATA, P2)
    """
    catch_errors.check_for_period_error(data, period_1)
    catch_errors.check_for_period_error(data, period_2)

    macd = ema(data, period_1) - ema(data, period_2)
    return macd
