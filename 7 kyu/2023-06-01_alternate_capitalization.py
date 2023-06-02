# Given a string, capitalize the letters that occupy even indexes and odd
#  indexes separately, and return as shown below. Index 0 will be
# considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for
# more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

# If you like this Kata, please try:

# Indexed capitalization

# Even-odd disparity


def capitalize(s):
    evens_caps = "".join(
        [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))]
    )  # noqa
    odds_caps = "".join(
        [s[i] if i % 2 == 0 else s[i].upper() for i in range(len(s))]
    )  # noqa
    return [evens_caps, odds_caps]


def capitalize2(s):
    result = ["", ""]
    for i, c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result
