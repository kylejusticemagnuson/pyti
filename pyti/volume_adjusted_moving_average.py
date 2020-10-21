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


def volume_adjusted_moving_average(close_data, volume, period):
    """
    Volume Adjusted Moving Average.

    Formula:
    VAMA = SUM(CLOSE * VolumeRatio) / period
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    catch_errors.check_for_period_error(close_data, period)

    avg_vol = np.mean(volume)
    vol_incr = avg_vol * 0.67
    vol_ratio = [val / vol_incr for val in volume]
    close_vol = np.array(close_data) * vol_ratio
    vama = [
        sum(close_vol[idx + 1 - period:idx + 1]) / period
        for idx in range(period - 1, len(close_data))
    ]
    vama = fill_for_noncomputable_vals(close_data, vama)
    return vama
