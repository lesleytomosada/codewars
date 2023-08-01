# Write a program that will calculate the number of trailing zeros in a
# factorial of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find
# the number of zeros.


import math


def zeros(n):
    z = 0
    if n != 0:
        k = math.log(n, 5)
        for i in range(1, int(k) + 1):
            z += int(n / 5**i)
    return z


def zeros2(n):
    """
    No factorial is going to have fewer zeros than the factorial of a smaller
    number.

    Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
    smaller than `n` (`n // 5`).

    Each multiple of 25 adds two 0's, so next we add another 0 for each
    # multiple of 25 smaller than n.

    We continue on for all powers of 5 smaller than (or equal to) n.
    """
    pow_of_5 = 5
    zeros = 0

    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5

    return zeros
