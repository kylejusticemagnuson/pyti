from __future__ import absolute_import
import numpy as np


def fill_for_noncomputable_vals(input_data, result_data):
    if isinstance(result_data, map):
        # if result is a map (map() in python 3 returns not a list but a map)
        result_data = list(result_data)

    non_computable_values = np.repeat(
        np.nan, len(input_data) - len(result_data)
        )
    filled_result_data = np.append(non_computable_values, result_data)
    return filled_result_data
