# pyti

This library contains various financial technical indicators that can be used to analyze financial data.

The complete list of indicators in this library:
```
Accumulation/Distribution
Aroon
  -Aroon Up
  -Aroon Down
Average Directional Index
Average True Range
Average True Range Percent
Bollinger Bands
  -Upper Bollinger Band
  -Middle Bollinger Band
  -Lower Bollinger Band
  -Bandwidth
  -Percent Bandwidth
  -Range
Chaikin Money Flow
Chande Momentum Oscillator
Commodity Channel Index
Detrended Price Oscillator
Double Exponential Moving Average
Double Smoothed Stochastic
Exponential Moving Average
Hull Moving Average
Ichimoku Cloud
  -TenkanSen
  -KijunSen
  -Chiku Span
  -Senkou A
  -Senkou B
Keltner Bands
  -Bandwidth
  -Center Band
  -Upper Band
  -Lower Band
Linear Weighted Moving Average
Momentum
Money Flow
Money Flow Index
Moving Average Convergence Divergence
Moving Average Envelope
  -Upper Band
  -Center Band
  -Lower Band
Negative Directional Index (-DI)
Negative Directional Movement (-DM)
On Balance Volume
Positive Directional Index (+DI)
Positive Directional Movement (+DM)
Price Channels
  -Upper Price Channel
  -Lower Price Channel
Price Oscillator
Simple Moving Average
Smoothed Moving Average
Standard Deviation
Standard Variance
Stochastic
  -%K
  -%D
Rate of Change
Relative Strength Index
Triangular Moving Average
Triple Exponential Moving Average
True Range
Typical Price
Vertical Horizontal Filter
Volatility
Volume Index
  -Positive Volume Index
  -Negative Volume Index
Weighted Moving Average
```
pyti is currently only compatible with Python 2.7

Install using pip:
```
pip install pyti
```

Simple example usage of library:
```python
from pyti.exponential_moving_average import exponential_moving_average as ema

data = [6, 7, 3, 6, 3, 9, 5]
period = 2
res = ema(data, period)

# res = [np.nan, 6.75, 4.0, 5.25, 3.75, 7.5, 6.0]
```
