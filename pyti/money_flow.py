from __future__ import absolute_import
from pyti import catch_errors
from pyti.typical_price import typical_price as tp


def money_flow(close_data, high_data, low_data, volume):
    """
    Money Flow.

    Formula:
    MF = VOLUME * TYPICAL PRICE
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume
        )
    mf = volume * tp(close_data, high_data, low_data)
    return mf
