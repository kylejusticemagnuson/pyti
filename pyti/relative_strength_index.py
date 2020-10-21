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
import numpy as np
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range
from six.moves import zip


def relative_strength_index(data, period):
    """
    Relative Strength Index.

    Formula:
    RSI = 100 - (100 / 1 + (prevGain/prevLoss))
    """
    catch_errors.check_for_period_error(data, period)

    period = int(period)
    changes = [
        data_tup[1] - data_tup[0] for data_tup in zip(data[::1], data[1::1])
    ]

    filtered_gain = [val < 0 for val in changes]
    gains = [
        0 if filtered_gain[idx] is True else changes[idx]
        for idx in range(0, len(filtered_gain))
    ]

    filtered_loss = [val > 0 for val in changes]
    losses = [
        0 if filtered_loss[idx] is True else abs(changes[idx])
        for idx in range(0, len(filtered_loss))
    ]

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    rsi = []
    if avg_loss == 0:
        rsi.append(100)
    else:
        rs = avg_gain / avg_loss
        rsi.append(100 - (100 / (1 + rs)))

    for idx in range(1, len(data) - period):
        avg_gain = (avg_gain * (period - 1) + gains[idx +
                                                    (period - 1)]) / period
        avg_loss = (avg_loss * (period - 1) + losses[idx +
                                                     (period - 1)]) / period

        if avg_loss == 0:
            rsi.append(100)
        else:
            rs = avg_gain / avg_loss
            rsi.append(100 - (100 / (1 + rs)))

    rsi = fill_for_noncomputable_vals(data, rsi)

    return rsi
