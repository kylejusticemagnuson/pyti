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
import warnings
from pyti.function_helper import fill_for_noncomputable_vals
from pyti import catch_errors
from six.moves import range


def simple_moving_average(data, period):
    """
    Simple Moving Average.

    Formula:
    SUM(data / N)
    """
    catch_errors.check_for_period_error(data, period)
    # Mean of Empty Slice RuntimeWarning doesn't affect output so it is
    # supressed
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        sma = [
            np.mean(data[idx - (period - 1):idx + 1])
            for idx in range(0, len(data))
        ]
    sma = fill_for_noncomputable_vals(data, sma)
    return sma
