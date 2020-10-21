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
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def exponential_moving_average(data, period):
    """
    Exponential Moving Average.

    Formula:
    p0 + (1 - w) * p1 + (1 - w)^2 * p2 + (1 + w)^3 * p3 +...
                /   1 + (1 - w) + (1 - w)^2 + (1 - w)^3 +...

    where: w = 2 / (N + 1)
    """
    catch_errors.check_for_period_error(data, period)
    emas = [
        exponential_moving_average_helper(data[idx - period + 1:idx + 1],
                                          period)
        for idx in range(period - 1, len(data))
    ]
    emas = fill_for_noncomputable_vals(data, emas)
    return emas


def exponential_moving_average_helper(data, period):
    w = 2 / float(period + 1)
    ema_top = data[period - 1]
    ema_bottom = 1
    for idx in range(1, period):  # idx 1 to n
        ema_top += ((1 - w)**idx) * data[period - 1 - idx]
        ema_bottom += (1 - w)**idx
    ema = ema_top / ema_bottom
    return ema
