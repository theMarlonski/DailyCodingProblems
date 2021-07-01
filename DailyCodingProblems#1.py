import pandas as pd
import numpy as np
import random

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
