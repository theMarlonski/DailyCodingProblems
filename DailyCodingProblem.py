import pandas as pd

"""
Task:
Given an array of integers, find the first missing
positive integer in linear time and constant space.
In other words, find the lowest positive integer
that does not exist in the array. The array can
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
"""

pos = []
def SmallestMissingPositive(array):
    for number in array:
        if number > 0:
            pos = pos.append(number)
    pos.sort()
    i = pos[1]
    solution = i - 1
    return solution

test_array = [4,5,2,-2,0,-5,2]
print(SmallestMissingPositive(test_array)) 