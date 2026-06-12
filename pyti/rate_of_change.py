from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals


def rate_of_change(data, period):
    """
    Rate of Change.

    Formula:
    (Close - Close n periods ago) / (Close n periods ago) * 100
    """
    catch_errors.check_for_period_error(data, period)

    rocs = [((data[idx] - data[idx - period]) /
         data[idx - period]) * 100 for idx in range(period, len(data))]
    rocs = fill_for_noncomputable_vals(data, rocs)
    return rocs
