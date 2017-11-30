# pyti

This library contains various financial technical indicators that can be used to analyze data.

Now compatible with both Python 2.7 and Python 3.6

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
  -%B
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
StochRSI
Rate of Change
Relative Strength Index
Triangular Moving Average
Triple Exponential Moving Average
True Range
Typical Price
Ultimate Oscillator
Vertical Horizontal Filter
Volatility
Volume Adjusted Moving Average
Volume Index
  -Positive Volume Index
  -Negative Volume Index
Volume Oscillator
Weighted Moving Average
Williams %R
```

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

Running the whole test suite using tox:
```
tox
```

To run tests for just Python 2.7 use
```
tox -e py27 tests
```
or just for Python 3.6
```
tox -e py36 tests
```

To specifically run one test in a specific Python version:
```
tox -e py36 -- tests/test_file_you_want_to_test:TestClassName.test_method_name
```

If there is an indicator that you would like to see added or believe there is an error in one of the existing ones, feel free to submit it to Issues. 
If you would like to add your own indicator, fork the project and submit a pull request. Contributions are always welcome.
