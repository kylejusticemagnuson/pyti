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
from pyti.typical_price import typical_price
from pyti.simple_moving_average import simple_moving_average as sma


def commodity_channel_index(close_data, high_data, low_data, period):
    """
    Commodity Channel Index.

    Formula:
    CCI = (TP - SMA(TP)) / (0.015 * Mean Deviation)
    """
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data)
    catch_errors.check_for_period_error(close_data, period)
    tp = typical_price(close_data, high_data, low_data)
    cci = (tp - sma(tp, period)) / (0.015 *
                                    np.mean(np.absolute(tp - np.mean(tp))))
    return cci
