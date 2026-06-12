"""
Cross-checks of pyti indicators against independent reference
implementations built from pandas primitives, plus hand-computed values on
tiny series. These exist so the per-indicator regression tests (whose
expected arrays were generated from pyti itself) are anchored to an
external source of truth.
"""
import unittest
import numpy as np
import pandas as pd

from tests.sample_data import SampleData
from pyti import (
    aroon,
    average_true_range,
    detrended_price_oscillator,
    directional_indicators,
    double_exponential_moving_average,
    exponential_moving_average,
    ichimoku_cloud,
    linear_weighted_moving_average,
    momentum,
    money_flow_index,
    moving_average_convergence_divergence,
    rate_of_change,
    relative_strength_index,
    simple_moving_average,
    smoothed_moving_average,
    triple_exponential_moving_average,
    true_range,
    ultimate_oscillator,
    weighted_moving_average,
    williams_percent_r,
)


def ref_ema(s, period):
    """EMA seeded with the SMA of the first `period` valid values, then
    recursed by pandas' ewm engine. Skips leading NaNs."""
    first = s.first_valid_index()
    valid = s.loc[first:]
    sub = valid.iloc[period - 1:].copy()
    sub.iloc[0] = valid.iloc[:period].mean()
    return sub.ewm(alpha=2.0 / (period + 1), adjust=False).mean().reindex(s.index)


def ref_smma(s, period):
    """Wilder smoothing via pandas' ewm engine, SMA-seeded."""
    first = s.first_valid_index()
    valid = s.loc[first:]
    sub = valid.iloc[period - 1:].copy()
    sub.iloc[0] = valid.iloc[:period].mean()
    return sub.ewm(alpha=1.0 / period, adjust=False).mean().reindex(s.index)


def ref_true_range(c, h, l):
    tr = pd.concat(
        [h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1
        ).max(axis=1)
    return tr


def assert_close(actual, expected_series):
    np.testing.assert_allclose(
        np.asarray(actual, dtype=float),
        expected_series.to_numpy(dtype=float),
        rtol=1e-9,
        equal_nan=True,
        )


class TestReferenceParity(unittest.TestCase):
    def setUp(self):
        data = SampleData()
        self.c = pd.Series(data.get_sample_close_data())
        self.h = pd.Series(data.get_sample_high_data())
        self.l = pd.Series(data.get_sample_low_data())
        self.v = pd.Series(data.get_sample_volume())

    def test_simple_moving_average(self):
        for period in (6, 10):
            assert_close(
                simple_moving_average.simple_moving_average(
                    list(self.c), period),
                self.c.rolling(period).mean(),
                )

    def test_exponential_moving_average(self):
        for period in (6, 10):
            assert_close(
                exponential_moving_average.exponential_moving_average(
                    list(self.c), period),
                ref_ema(self.c, period),
                )

    def test_smoothed_moving_average(self):
        for period in (6, 10):
            assert_close(
                smoothed_moving_average.smoothed_moving_average(
                    list(self.c), period),
                ref_smma(self.c, period),
                )

    def test_weighted_moving_average(self):
        period = 6
        weights = np.arange(1, period + 1)
        ref = self.c.rolling(period).apply(
            lambda w: (w * weights).sum() / weights.sum(), raw=True)
        assert_close(
            weighted_moving_average.weighted_moving_average(
                list(self.c), period),
            ref,
            )
        assert_close(
            linear_weighted_moving_average.linear_weighted_moving_average(
                list(self.c), period),
            ref,
            )

    def test_lwma_handles_duplicate_values(self):
        # the pre-0.3.0 implementation looked weights up by value, so
        # duplicates inside a window all got the first occurrence's weight
        lwma = linear_weighted_moving_average.linear_weighted_moving_average(
            [1.0, 2.0, 2.0, 3.0], 3)
        np.testing.assert_allclose(
            lwma, [np.nan, np.nan, 11.0 / 6.0, 15.0 / 6.0], equal_nan=True)

    def test_macd_dema_tema(self):
        e6 = ref_ema(self.c, 6)
        assert_close(
            moving_average_convergence_divergence
            .moving_average_convergence_divergence(list(self.c), 6, 12),
            e6 - ref_ema(self.c, 12),
            )
        assert_close(
            double_exponential_moving_average
            .double_exponential_moving_average(list(self.c), 6),
            2 * e6 - ref_ema(e6, 6),
            )
        assert_close(
            triple_exponential_moving_average
            .triple_exponential_moving_average(list(self.c), 6),
            3 * e6 - 3 * ref_ema(e6, 6) + ref_ema(ref_ema(e6, 6), 6),
            )

    def test_true_range(self):
        assert_close(
            true_range.true_range(list(self.c), list(self.h), list(self.l)),
            ref_true_range(self.c, self.h, self.l),
            )

    def test_average_true_range(self):
        period = 14
        assert_close(
            average_true_range.average_true_range(
                list(self.c), list(self.h), list(self.l), period),
            ref_smma(ref_true_range(self.c, self.h, self.l), period),
            )

    def test_relative_strength_index(self):
        period = 14
        delta = self.c.diff()
        avg_gain = ref_smma(delta.clip(lower=0).iloc[1:], period)
        avg_loss = ref_smma((-delta.clip(upper=0)).iloc[1:], period)
        ref = (100 - 100 / (1 + avg_gain / avg_loss)).reindex(self.c.index)
        assert_close(
            relative_strength_index.relative_strength_index(
                list(self.c), period),
            ref,
            )

    def test_money_flow_index(self):
        period = 14
        tp = (self.h + self.l + self.c) / 3
        mf = tp * self.v
        pos = mf.where(tp > tp.shift(), 0.0)
        neg = mf.where(tp < tp.shift(), 0.0)
        pos.iloc[0] = np.nan
        neg.iloc[0] = np.nan
        ratio = pos.rolling(period).sum() / neg.rolling(period).sum()
        ref = 100 - 100 / (1 + ratio)
        assert_close(
            money_flow_index.money_flow_index(
                list(self.c), list(self.h), list(self.l), list(self.v),
                period),
            ref,
            )

    def test_williams_percent_r(self):
        period = 14
        hh = self.h.rolling(period).max()
        ll = self.l.rolling(period).min()
        ref = (hh - self.c) / (hh - ll) * -100
        assert_close(
            williams_percent_r.williams_percent_r(
                list(self.c), list(self.h), list(self.l), period),
            ref,
            )

    def test_momentum_and_rate_of_change(self):
        period = 10
        assert_close(
            momentum.momentum(list(self.c), period),
            self.c.diff(period),
            )
        assert_close(
            rate_of_change.rate_of_change(list(self.c), period),
            self.c.diff(period) / self.c.shift(period) * 100,
            )

    def test_aroon(self):
        period = 25
        ref_up = self.c.rolling(period + 1).apply(
            lambda w: (period - (len(w) - 1 - np.argmax(w))) / period * 100,
            raw=True)
        ref_down = self.c.rolling(period + 1).apply(
            lambda w: (period - (len(w) - 1 - np.argmin(w))) / period * 100,
            raw=True)
        assert_close(aroon.aroon_up(list(self.c), period), ref_up)
        assert_close(aroon.aroon_down(list(self.c), period), ref_down)

    def test_detrended_price_oscillator(self):
        period = 10
        ref = self.c - self.c.rolling(period).mean().shift(period // 2 + 1)
        assert_close(
            detrended_price_oscillator.detrended_price_oscillator(
                list(self.c), period),
            ref,
            )

    def test_chiku_span(self):
        assert_close(
            ichimoku_cloud.chiku_span(list(self.c)),
            self.c.shift(-26),
            )

    def test_ultimate_oscillator(self):
        pc = self.c.shift()
        bp = self.c - pd.concat([self.l, pc], axis=1).min(axis=1)
        bp.iloc[0] = np.nan
        tr = ref_true_range(self.c, self.h, self.l)

        def avg(period):
            return bp.rolling(period).sum() / tr.rolling(period).sum()

        ref = 100 * (4 * avg(7) + 2 * avg(14) + avg(28)) / 7
        assert_close(
            ultimate_oscillator.ultimate_oscillator(
                list(self.c), list(self.h), list(self.l)),
            ref,
            )

    def test_directional_indicators(self):
        period = 14
        up = self.h.diff()
        down = -self.l.diff()
        pdm = up.where((up > down) & (up > 0), 0.0)
        ndm = down.where((down > up) & (down > 0), 0.0)
        atr = ref_smma(ref_true_range(self.c, self.h, self.l), period)
        pdi = 100 * ref_smma(pdm.iloc[1:], period).reindex(self.c.index) / atr
        ndi = 100 * ref_smma(ndm.iloc[1:], period).reindex(self.c.index) / atr
        adx = ref_smma(100 * (pdi - ndi).abs() / (pdi + ndi),
                       period).reindex(self.c.index)

        args = (list(self.c), list(self.h), list(self.l), period)
        assert_close(
            directional_indicators.positive_directional_index(*args), pdi)
        assert_close(
            directional_indicators.negative_directional_index(*args), ndi)
        assert_close(
            directional_indicators.average_directional_index(*args), adx)
