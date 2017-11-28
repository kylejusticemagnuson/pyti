from __future__ import absolute_import
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def rate_of_change(data, period):
    """
    Rate of Change.

    Formula:
    (Close - Close n periods ago) / (Close n periods ago) * 100
    """
    catch_errors.check_for_period_error(data, period)

    rocs = [((data[idx] - data[idx - (period - 1)]) /
         data[idx - (period - 1)]) * 100 for idx in range(period - 1, len(data))]
    rocs = fill_for_noncomputable_vals(data, rocs)
    return rocs
