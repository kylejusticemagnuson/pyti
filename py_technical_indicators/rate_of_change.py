from py_technical_indicators import catch_errors
from py_technical_indicators.function_helper import fill_for_noncomputable_vals


def rate_of_change(data, period):
    """
    Rate of Change

    Formula:
    (Close - Close n periods ago) / (Close n periods ago) * 100
    """
    catch_errors.check_for_period_error(data, period)

    rocs = map(
        lambda idx:
        ((data[idx] - data[idx - (period - 1)]) /
         data[idx - (period - 1)]) * 100,
        range(period - 1, len(data))
        )
    rocs = fill_for_noncomputable_vals(data, rocs)
    return rocs
