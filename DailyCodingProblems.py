import pandas as pd
import numpy as np
import random
import itertools

# Problem 1

"""Task: 
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.
"""


def ProblemSolver(numberslist, k):
    for i in range(0, len(numberslist)):
        for j in range(i + 1, len(numberslist)):
            if numberslist[i] + numberslist[j] == k:
                return True
    return False


numbers = random.sample(range(0, 1000000), k=10000)
goal = random.random

ProblemSolver(numbers, goal)

# Works, but not time efficient with very large lists

# Problem2

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


# Problem3

# Problem4

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
            pos.append(number)
    pos.sort()
    i = pos[1]
    solution = i - 1
    if solution == 0:
        return "There is no lower, missing positive integer"
    else:
        return solution


test_array = [0.4, 1, 2, 3, 4, 5]
print(SmallestMissingPositive(test_array))


# Problem5

"""
Problem:

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# Problem6

# Problem7

# Problem8
