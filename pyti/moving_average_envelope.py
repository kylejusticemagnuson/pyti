'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



from __future__ import absolute_import
from pyti.simple_moving_average import simple_moving_average as sma


def center_band(data, period):
    """
    Center Band.

    Formula:
    SMA(data)
    """
    cb = sma(data, period)
    return cb


def upper_band(data, period, env_percentage):
    """
    Upper Band.

    Formula:
    ub = cb(t) * (1 + env_percentage)
    """
    cb = center_band(data, period)
    ub = [val * (1 + float(env_percentage)) for val in cb]
    return ub


def lower_band(data, period, env_percentage):
    """
    Lower Band.

    Formula:
    lb = cb * (1 - env_percentage)
    """
    cb = center_band(data, period)
    lb = [val * (1 - float(env_percentage)) for val in cb]
    return lb
