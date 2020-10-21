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



def check_for_period_error(data, period):
    """
    Check for Period Error.

    This method checks if the developer is trying to enter a period that is
    larger than the data set being entered. If that is the case an exception is
    raised with a custom message that informs the developer that their period
    is greater than the data set.
    """
    period = int(period)
    data_len = len(data)
    if data_len < period:
        raise Exception("Error: data_len < period")


def check_for_input_len_diff(*args):
    """
    Check for Input Length Difference.

    This method checks if multiple data sets that are inputted are all the same
    size. If they are not the same length an error is raised with a custom
    message that informs the developer that the data set's lengths are not the
    same.
    """
    arrays_len = [len(arr) for arr in args]
    if not all(a == arrays_len[0] for a in arrays_len):
        err_msg = ("Error: mismatched data lengths, check to ensure that all "
                   "input data is the same length and valid")
        raise Exception(err_msg)
