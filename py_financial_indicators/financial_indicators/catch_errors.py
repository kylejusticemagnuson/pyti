
def check_for_period_error(data, period):
    period = int(period)
    data_len = len(data)
    if data_len < period:
        # raise exception with message
        raise Exception('Error: data_len < period')
