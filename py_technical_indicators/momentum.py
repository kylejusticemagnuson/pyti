from py_technical_indicators import catch_errors
from py_technical_indicators.function_helper import fill_for_noncomputable_vals


def momentum(data, period):
    """
    Momentum.
    DATA[i] - DATA[i - period]
    """
    catch_errors.check_for_period_error(data, period)

    momentum = map(
        lambda idx:
        data[idx] - data[idx+1-period],
        range(period-1, len(data))
        )
    momentum = fill_for_noncomputable_vals(data, momentum)
    return momentum
