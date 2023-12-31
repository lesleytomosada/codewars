# DESCRIPTION:
# Write a function that takes an array of numbers (integers for the tests) and
#  a target number. It should find two different items in the array that, when
# added together, give the target value. The indices of these items should then
# be returned in a tuple / list (depending on your language) like so: (index1,
# index2).

# For the purposes of this kata, some tests may have multiple answers; any
# valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or
# greater, and all of the items will be numbers; target will always be the
# sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/

# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]


def two_sum(numbers, target):
    num_set = set(numbers)
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in num_set:
            idx = numbers.index(diff, i + 1)
            return (i, idx)


def two_sum2(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
