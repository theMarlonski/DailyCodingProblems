import pandas as pd


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair
