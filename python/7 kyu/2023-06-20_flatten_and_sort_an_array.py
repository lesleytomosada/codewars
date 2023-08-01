# Challenge:

# Given a two-dimensional array of integers, return the flattened version of
# the array with all the integers in the sorted (ascending) order.

# Example:

# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1,
# 2, 3, 4, 5, 6, 7, 8, 9].


def flatten_and_sort(array):
    res = []
    for arr in array:
        for i in range(len(arr)):
            res.append(arr[i])
    return sorted(res)


def flatten_and_sort2(array):
    newList = []
    for item in array:
        newList += item
    return sorted(newList)
