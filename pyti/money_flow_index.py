import numpy as np
import warnings
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from pyti.typical_price import typical_price
from pyti.money_flow import money_flow


def money_flow_index(close_data, high_data, low_data, volume, period):
    """
    Money Flow Index.

    Formula:
    MFI = 100 - (100 / (1 + PMF / NMF))
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume
        )
    catch_errors.check_for_period_error(close_data, period)

    mf = money_flow(close_data, high_data, low_data, volume)
    tp = typical_price(close_data, high_data, low_data)

    pf = [mf[idx] if tp[idx] > tp[idx-1] else 0 for idx in range(1, len(tp))]
    nf = [mf[idx] if tp[idx] < tp[idx-1] else 0 for idx in range(1, len(tp))]

    pmf = [sum(pf[idx+1-period:idx+1]) for idx in range(period-1, len(pf))]
    nmf = [sum(nf[idx+1-period:idx+1]) for idx in range(period-1, len(nf))]

    # Dividing by 0 is not an issue, it turns the value into NaN which we would
    # want in that case
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        money_ratio = np.array(pmf) / np.array(nmf)

    mfi = 100 - (100 / (1 + money_ratio))

    mfi = fill_for_noncomputable_vals(close_data, mfi)

    return mfi
