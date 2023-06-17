# There is an array with some numbers. All numbers are equal except for one.
# Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string
# Find The Unique


def find_uniq(arr):
    values = list(set(arr))
    beg = arr[:3]
    counts = []
    for val in values:
        counts.append(beg.count(val))
    if counts[0] > counts[1]:
        return values[1]
    else:
        return values[0]


def find_uniq2(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]
