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
from six.moves import range


def on_balance_volume(close_data, volume):
    """
    On Balance Volume.

    Formula:
    start = 1
    if CLOSEt > CLOSEt-1
        obv = obvt-1 + volumet
    elif CLOSEt < CLOSEt-1
        obv = obvt-1 - volumet
    elif CLOSEt == CLOSTt-1
        obv = obvt-1
    """
    catch_errors.check_for_input_len_diff(close_data, volume)
    obv = np.zeros(len(volume))
    obv[0] = 1
    for idx in range(1, len(obv)):
        if close_data[idx] > close_data[idx - 1]:
            obv[idx] = obv[idx - 1] + volume[idx]
        elif close_data[idx] < close_data[idx - 1]:
            obv[idx] = obv[idx - 1] - volume[idx]
        elif close_data[idx] == close_data[idx - 1]:
            obv[idx] = obv[idx - 1]
    return obv
