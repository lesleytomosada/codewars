# My friend John and I are members of the "Fat to Fit Club (FFC)". John is
# worried because each month a list with the weights of members is published
# and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more,
# I will modify the order of the list". It was decided to attribute a "weight"
# to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list
# 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give
# this string ordered by "weights" of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:

# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were
# strings (alphabetical ordering) and not numbers:

# 180 is before 90 since, having the same "weight" (9), it comes before as a
# string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing whitespaces and
# more than a unique whitespace between two consecutive numbers
# For C: The result is freed.


def order_weight(strng):
    orig_weights = strng.split()
    new_weights = []
    for weight in orig_weights:
        total = 0
        for i in range(len(weight)):
            total += int(weight[i])
        new_weights.append([total, weight])
    new_weights.sort()
    res = []
    for weight in new_weights:
        res.append(weight[1])
    return " ".join(res)


def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


def order_weight2(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))

    return result
