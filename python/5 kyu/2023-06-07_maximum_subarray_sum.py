# DESCRIPTION:
# The maximum sum subarray problem consists in finding the maximum sum of a
# contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the
# maximum sum is the sum of the whole array. If the list is made up of only
# negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list
# or array is also a valid sublist/subarray.


def max_sequence(arr):
    if len(arr) == 0 or max(arr) < 0:
        return 0
    if min(arr) > 0:
        return sum(arr)

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


def maxSequence2(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max:
            max = curr
    return max
