import numpy as np
from py_ti import catch_errors
from py_ti.function_helper import fill_for_noncomputable_vals


def conversion_base_line_helper(data, period):
    """
    The only real difference between TenkanSen and KijunSen is the period value
    """
    catch_errors.check_for_period_error(data, period)
    cblh = map(
        lambda idx:
        (np.max(data[idx+1-period:idx+1]) -
            np.min(data[idx+1-period:idx+1])) / 2,
        range(period-1, len(data))
        )

    cblh = fill_for_noncomputable_vals(data, cblh)
    return cblh


def tenkansen(data, period=9):
    """
    TenkanSen (Conversion Line)
    (H + L) / 2  :: default period=9
    """
    ts = conversion_base_line_helper(data, period)
    return ts


def kijunsen(data, period=26):
    """
    KijunSen (Base Line)
    (H + L) / 2  :: default period=26
    """
    ks = conversion_base_line_helper(data, period)
    return ks


def chiku_span(data):
    """
    Chiku Span (Lagging Span)
    Close shifted back 26 bars
    """
    cs = data[25::]
    return cs


def senkou_a(data):
    """
    Senkou A (Leading Span A)
    (TenkanSen + KijunSen) / 2 :: Shift Forward 26 bars
    """
    sa = (tenkansen(data) + kijunsen(data)) / 2
    # shift forward
    shift_by = np.repeat(np.nan, 26)
    sa = np.append(shift_by, sa)
    return sa


def senkou_b(data, period=52):
    """
    Senkou B (Leading Span B)
    (H + L) / 2  :: default period=52 :: shifted forward 26 bars
    """
    sb = conversion_base_line_helper(data, period)
    shift_by = np.repeat(np.nan, 26)
    sb = np.append(shift_by, sb)
    return sb
