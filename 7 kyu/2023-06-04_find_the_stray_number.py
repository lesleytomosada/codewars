# DESCRIPTION:
# You are given an odd-length array of integers, in which all of them are the
# same, except for one single number.

# Complete the method which accepts such an array, and returns that single
# different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3


def stray(arr):
    dict = {}
    for num in arr:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1

    for k, v in dict.items():
        if v % 2 != 0:
            return k


def stray2(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]
