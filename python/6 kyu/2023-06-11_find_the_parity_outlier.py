# DESCRIPTION:
# You are given an array (which will have a length of at least 3, but could be
# very large) containing integers. The array is either entirely comprised of
# odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns
# this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    evens = 0
    odds = 0
    test = [integers[0], integers[1], integers[2]]
    for item in test:
        if item % 2 == 0:
            evens += 1
        else:
            odds += 1

    if evens > odds:
        for num in integers:
            if num % 2 != 0:
                return num
    else:
        for num in integers:
            if num % 2 == 0:
                return num


def find_outlier2(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
