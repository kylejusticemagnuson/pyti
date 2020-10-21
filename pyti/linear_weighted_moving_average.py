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


def linear_weighted_moving_average(data, period):
    """
    Linear Weighted Moving Average.

    Formula:
    LWMA = SUM(DATA[i]) * i / SUM(i)
    """
    catch_errors.check_for_period_error(data, period)

    idx_period = list(range(1, period + 1))
    lwma = [(sum([
        i * idx_period[data[idx - (period - 1):idx + 1].index(i)]
        for i in data[idx - (period - 1):idx + 1]
    ])) / sum(range(1,
                    len(data[idx + 1 - period:idx + 1]) + 1))
            for idx in range(period - 1, len(data))]
    lwma = fill_for_noncomputable_vals(data, lwma)
    return lwma
