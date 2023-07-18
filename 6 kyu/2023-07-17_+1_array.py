# Given an array of integers of any length, return an array that has 1 added
# to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# Valid arrays

# [4, 3, 2, 5] would return [4, 3, 2, 6]
# [1, 2, 3, 9] would return [1, 2, 4, 0]
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0]
# [0, 1, 3, 7] would return [0, 1, 3, 8]

# Invalid arrays

# [1, -9] is invalid because -9 is not a non-negative integer

# [1, 2, 33] is invalid because 33 is not a single-digit integer


def up_array(arr):
    if not arr:
        return None
    for num in arr:
        if num < 0:
            return None
        elif num > 9:
            return None

    res = []
    st = ""
    for num in arr:
        st += str(num)

    num = int(st) + 1

    if len(arr) > len(str(num)):
        diff = len(arr) - len(str(num))
        res = [0] * diff

    for number in str(num):
        res.append(int(number))

    return res


def up_array1(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None

    for i in range(len(arr) - 1, -1, -1):
        arr[i] += 1
        if arr[i] < 10:
            return arr
        else:
            arr[i] = 0

    return [1] + arr
