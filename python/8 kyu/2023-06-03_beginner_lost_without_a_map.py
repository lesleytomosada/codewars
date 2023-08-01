# DESCRIPTION:
# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]


def maps(a):
    return list(map(lambda x: 2 * x, a))


def maps2(a):
    return [2 * x for x in a]
