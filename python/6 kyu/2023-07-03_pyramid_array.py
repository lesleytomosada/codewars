# Write a function that when given a number >= 0, returns an Array of
# ascending length subarrays.

# pyramid(0) => [ ]
# pyramid(1) => [ [1] ]
# pyramid(2) => [ [1], [1, 1] ]
# pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
# Note: the subarrays should be filled with 1s


def pyramid(n):
    res = []
    if n < 1:
        return res
    for i in range(1, n + 1):
        res.append([1] * i)
    return res


def pyramid1(n):
    return [[1] * x for x in range(1, n + 1)]
