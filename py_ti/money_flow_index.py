import numpy as np
import warnings
from py_ti import catch_errors
from py_ti.function_helper import fill_for_noncomputable_vals
from py_ti.typical_price import typical_price
from py_ti.money_flow import money_flow


def money_flow_index(close_data, high_data, low_data, volume, period):
    """
    Money Flow Index
    MFI = 100 - (100 / (1 + PMF / NMF))
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume
        )
    catch_errors.check_for_period_error(close_data, period)

    mf = money_flow(close_data, high_data, low_data, volume)
    tp = typical_price(close_data, high_data, low_data)

    flow = map(lambda idx: tp[idx] > tp[idx-1], range(1, len(tp)))
    pf = map(lambda idx: mf[idx] if flow[idx] else 0, range(0, len(flow)))
    nf = map(lambda idx: mf[idx] if not flow[idx] else 0, range(0, len(flow)))

    pmf = map(
        lambda idx:
        sum(pf[idx+1-period:idx+1]),
        range(period-1, len(pf))
        )
    nmf = map(
        lambda idx:
        sum(nf[idx+1-period:idx+1]),
        range(period-1, len(nf))
        )

    # Dividing by 0 is not an issue, it turns the value into NaN which we would
    # want in that case
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        money_ratio = np.array(pmf) / np.array(nmf)

    mfi = 100 - (100 / (1 + money_ratio))

    mfi = fill_for_noncomputable_vals(close_data, mfi)

    return mfi
