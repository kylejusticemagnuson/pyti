from pyti.weighted_moving_average import weighted_moving_average


def linear_weighted_moving_average(data, period):
    """
    Linear Weighted Moving Average.

    Formula:
    LWMA = (P1 + 2 P2 + 3 P3 + ... + n Pn) / K
    where K = (1+2+...+n) = n(n+1)/2 and Pn is the most recent price
    """
    return weighted_moving_average(data, period)
