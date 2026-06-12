# Changelog

## 0.3.0 (2026-06-12)

Breaking modernization release. The library now requires Python 3.10+
(tested through 3.14) and depends only on numpy at runtime (pandas and six
dropped). Packaging moved from `setup.py`/tox/nose to `pyproject.toml`,
pytest, and a GitHub Actions test matrix.

### Bug fixes

- **linear_weighted_moving_average**: weights were looked up by value
  (`list.index`), so duplicate prices inside a window all received the first
  occurrence's weight. Now a true positional weighted average (identical to
  `weighted_moving_average`).
- **money_flow_index**: off-by-one — each bar's money flow was classified by
  the *next* bar's price direction, and the final bar was never counted.
- **relative_strength_index**: silently returned wrong values for numpy array
  input (an `is True` check that only worked with Python bools). List input
  was unaffected.
- **packaging**: `six` was imported throughout but never declared as a
  dependency, breaking clean installs. Removed entirely.

### Breaking changes — indicators reworked to textbook definitions

All of these change numeric output; functions marked with (signature) also
take new arguments.

- **exponential_moving_average**: was a truncated weighted average over only
  `period` bars; now the standard recursive EMA (alpha = 2/(N+1)) seeded with
  the SMA of the first N values. Affects MACD, DEMA, TEMA, price oscillator,
  price channels, and double smoothed stochastic.
- **smoothed_moving_average**: was `pandas.ewm(alpha=1/N)` with
  `adjust=True` from bar 0; now Wilder's smoothing seeded with the SMA of the
  first N values. Affects ATR and the directional indicators.
- **true_range** (signature): now `true_range(close, high, low)` computing
  the per-bar textbook TR; previously approximated high/low from a rolling
  window of closes and took a `period`.
- **average_true_range / average_true_range_percent** (signature): now
  `(close, high, low, period)`; ATR is Wilder smoothing of the new TR and the
  warm-up region is NaN instead of raw TR values.
- **ultimate_oscillator** (signature): now `(close, high, low)` using
  textbook buying pressure and true range.
- **williams_percent_r** (signature): now `(close, high, low, period)` over a
  rolling window; previously ignored periods and used the whole dataset's
  max/min of closes.
- **positive/negative_directional_movement**: first value is now NaN instead
  of 0, so the +DI/−DI Wilder seed is not polluted; +DI/−DI/ADX pick up the
  corrected ATR and SMMA.
- **momentum / rate_of_change**: looked back `period - 1` bars despite
  documenting `period`; now `data[t] - data[t - period]` as documented.
- **aroon_up / aroon_down**: used a window of `period` bars so the output
  could never reach 0; now the standard `period + 1` bar window with the full
  0–100 range.
- **detrended_price_oscillator**: now the textbook
  `price - SMA(period) displaced (period/2 + 1) bars`; previously subtracted
  the mean of the last `period/2 + 1` closes.
- **ichimoku_cloud.chiku_span**: now the close shifted back 26 bars at full
  input length (trailing NaNs); previously returned a truncated copy shifted
  the wrong way.
- **catch_errors**: validation failures raise `ValueError` (a subclass of the
  previously raised `Exception`) with unchanged messages.

### Known quirks kept for compatibility (documented, not changed)

- `volume_adjusted_moving_average` normalizes by the whole series' average
  volume, which introduces lookahead.
- Bollinger bands use population standard deviation (ddof=0) while the
  `standard_deviation` indicator uses sample standard deviation (ddof=1);
  both are accepted conventions.

### Tooling

- `pyproject.toml` replaces `setup.py`, `setup.cfg`, `MANIFEST.in`,
  `requirements.txt`, and `tox.ini`.
- Tests run with pytest; expected values for every reworked indicator were
  regenerated and are cross-checked against independent pandas-based
  reference implementations in `tests/test_reference_parity.py`.
- CI: GitHub Actions matrix over Python 3.10–3.14.
