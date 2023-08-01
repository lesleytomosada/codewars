# Your task is to write function factorial.

# https://en.wikipedia.org/wiki/Factorial

# FUNDAMENTALS


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
