# Finish the solution so that it takes an input n (integer) and returns a
# string that is the decimal representation of the number grouped by commas
# after every 3 digits.

# Assume: 0 <= n < 2147483647

# Examples
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"
#    10000  ->      "10,000"
#   100000  ->     "100,000"
#  1000000  ->   "1,000,000"
# 35235235  ->  "35,235,235"


def group_by_commas(n):
    length = len(str(n))
    if length < 4:
        return str(n)

    pieces = []

    count = 0

    for i in range(length - 1, -1, -1):
        pieces.insert(0, str(n)[i])
        count += 1
        if count == 3:
            pieces.insert(0, ",")
            count = 0

    if pieces[0] == ",":
        pieces.pop(0)
    return "".join(pieces)


def group_by_commas1(n):
    n = [i for i in str(n)]
    for i in range(len(n) - 4, -1, -3):
        n.insert(i + 1, ",")
    return "".join(n)
