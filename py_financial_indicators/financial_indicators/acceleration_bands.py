import numpy as np

from financial_indicators.simple_moving_average import sma


def upper_band(data, period, factor=0.001):
    """
    Acceleration Bands: Upper Band

    Formula:
    High * (1 + 2) * ((((High - Low)/((High + Low)/2)) * 1000) * Factor)
    """
    upper = np.max(data) * (1 + 2 * ((((np.max(data) - np.min(data)) / ((np.max(data) + np.min(data)) / 2)) * 1000) * factor))
    upper_band = map(lambda value: value + upper, sma(data, period))
    return upper_band


def middle_band(data, period):
    """
    Acceleration Bands: Middle Band

    Formula:
    sma(data, period)
    """
    middle_band = sma(data, period)
    return middle_band


def lower_band(data, period, factor=0.001):
    """
    Acceleration Bands: Lower Band

    Formula:
    Low * (1 - 2) * ((((High - Low)/((High + Low)/2)) * 1000) * Factor)
    """
    lower = np.min(data) * (1 - 2 * ((((np.max(data) - np.min(data)) / ((np.max(data) + np.min(data)) / 2)) * 1000) * factor))
    print lower
    lower_band = map(lambda value: value - abs(lower), sma(data, period))
    return lower_band
