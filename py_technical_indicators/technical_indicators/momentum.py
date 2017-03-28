import numpy as np
import catch_errors


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
    non_computable_values = np.repeat(np.nan, len(data) - len(momentum))
    momentum = np.append(non_computable_values, momentum)
    return momentum
