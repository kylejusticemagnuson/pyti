import numpy as np
import catch_errors


def vertical_horizontal_filter(data, period):
    """
    Vertical Horizontal Filter
    ABS(pHIGH - pLOW) / SUM(ABS(Pi - Pi-1))
    """
    catch_errors.check_for_period_error(data, period)

    vhf = map(
        lambda idx:
        abs(np.max(data[idx+1-period:idx+1]) - np.min(data[idx+1-period:idx+1])) /
        sum(map(
            lambda i:
            abs(data[idx+1-period:idx+1][i] - data[idx+1-period:idx+1][i-1]),
            range(0, len(data[idx+1-period:idx+1])))),
        range(period - 1, len(data))
        )

    non_computable_values = np.repeat(np.nan, len(data) - len(vhf))
    vhf = np.append(non_computable_values, vhf)
    return vhf
