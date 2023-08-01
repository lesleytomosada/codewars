# DESCRIPTION:
# Given two arrays of strings a1 and a2 return a sorted array r in
# lexicographical order of the strings of a1 which are substrings of strings
# of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples
# in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are
# separated by commas.
# Beware: In some languages r must be without duplicates.

def in_array(array1, array2):
    r = []
    sorted_array1 = sorted(array1)
    concat_array2 = " ".join(array2)
    if array1 and array2:
        for word in sorted_array1:
            if word in concat_array2 and word not in r:
                r.append(word)
    return r


def in_array2(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and a1 not in res:
                res.append(a1)
    res.sort()
    return res
