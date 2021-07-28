import pandas as pd
import numpy as np

"""
Problem:

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

input_array = [1, 2, 3, 4, 5]


def array_multiplier(input_array):
    output_array = []
    for i in input_array:
        calculation_array = input_array.copy()
        calculation_array.remove(i)
        result = np.product(calculation_array)
        output_array.append(result)
    return output_array


array_multiplier(input_array)
