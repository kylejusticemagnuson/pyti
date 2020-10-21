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
from pyti.simple_moving_average import simple_moving_average as sma
from six.moves import range


def percent_k(data, period):
    """
    %K.

    Formula:
    %k = data(t) - low(n) / (high(n) - low(n))
    """
    catch_errors.check_for_period_error(data, period)
    percent_k = [((data[idx] - np.min(data[idx + 1 - period:idx + 1])) /
                  (np.max(data[idx + 1 - period:idx + 1]) -
                   np.min(data[idx + 1 - period:idx + 1])))
                 for idx in range(period - 1, len(data))]
    percent_k = fill_for_noncomputable_vals(data, percent_k)

    return percent_k


def percent_d(data, period):
    """
    %D.

    Formula:
    %D = SMA(%K, 3)
    """
    p_k = percent_k(data, period)
    percent_d = sma(p_k, 3)
    return percent_d
