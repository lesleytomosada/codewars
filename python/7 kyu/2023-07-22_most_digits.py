# Find the number with the most digits.

# If two numbers in the argument array have the same number of digits, return
# the first one in the array.


def find_longest(arr):
    length = 0
    max_num = 0
    for num in arr:
        if len(str(num)) > length:
            length = len(str(num))
            max_num = num

    return max_num


def find_longest1(xs):
    return max(xs, key=lambda x: len(str(x)))
