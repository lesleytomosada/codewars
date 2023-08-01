# DESCRIPTION:
# An isogram is a word that has no repeating letters, consecutive or non-
# consecutive. Implement a function that determines whether a string that
# contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter
#  case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false
from collections import defaultdict


def is_isogram(string):
    string = string.lower()
    dict = defaultdict(int)

    for letter in string:
        dict[letter] += 1

    for value in dict.values():
        if value > 1:
            return False
    return True


def is_isogram2(string):
    return len(string) == len(set(string.lower()))
