
def check_for_period_error(data, period):
    period = int(period)
    data_len = len(data)
    if data_len < period:
        raise Exception("Error: data_len < period")


def check_for_input_len_diff(*args):
    arrays_len = map(lambda arr: len(arr), args)
    if not all(a == arrays_len[0] for a in arrays_len):
        err_msg = ("Error: mismatched data lengths, check to ensure that all "
                   "input data is the same length and valid")
        raise Exception(err_msg)
