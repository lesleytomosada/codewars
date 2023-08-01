# Given a string s. You have to return another string such that even-indexed
# and odd-indexed characters of s are grouped and groups are space-separated
# (see sample below)

# Note:
# 0 is considered to be an even index.
# All input strings are valid with no spaces


def sort_my_string(s):
    evens = ""
    odds = ""
    for i in range(len(s)):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]

    return f"{evens} {odds}"


def sort_my_string1(s):
    return s[::2] + " " + s[1::2]
