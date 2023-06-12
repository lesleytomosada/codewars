# DESCRIPTION:
# You will be given a list of strings. You must sort it alphabetically (case-
# sensitive, and based on the ASCII values of the chars) and then return the
# first value.

# The returned value must be a string, and have "***" between each of its
# letters.

# You should not remove or add elements from/to the array.


def two_sort(array):
    return "***".join([c for c in sorted(array)[0]])


def two_sort2(arr):
    return "***".join(sorted(arr)[0])
