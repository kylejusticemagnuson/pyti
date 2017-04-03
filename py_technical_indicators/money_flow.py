from py_technical_indicators import catch_errors
from py_technical_indicators.typical_price import typical_price as tp


def money_flow(close_data, high_data, low_data, volume):
    """
    Money Flow.
    MF = VOLUME * TYPICAL PRICE
    """
    catch_errors.check_for_input_len_diff(
        close_data, high_data, low_data, volume
        )
    mf = volume * tp(close_data, high_data, low_data)
    return mf
