# You will be given an array and a limit value. You must check that all values
# in the array are below or equal to the limit value. If they are, return
# true. Else, return false.

# You can assume all values in the array are numbers.


def small_enough(array, limit):
    for x in array:
        if x > limit:
            return False

    return True


def small_enough2(array, limit):
    return max(array) <= limit
