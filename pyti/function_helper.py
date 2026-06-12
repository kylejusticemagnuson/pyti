import numpy as np


def fill_for_noncomputable_vals(input_data, result_data):
    non_computable_values = np.repeat(
        np.nan, len(input_data) - len(result_data)
        )
    filled_result_data = np.append(non_computable_values, result_data)
    return filled_result_data


def first_computable_index(data):
    """
    Index of the first non-NaN value, so indicators can be chained without
    a previous indicator's warm-up NaNs poisoning the whole series.
    Returns len(data) if every value is NaN.
    """
    finite = np.where(~np.isnan(np.asarray(data, dtype=float)))[0]
    return int(finite[0]) if len(finite) else len(data)
