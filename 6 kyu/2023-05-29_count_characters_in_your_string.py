# https://www.codewars.com/kata/52efefcbcdf57161d4000091/solutions/python

# DESCRIPTION:
# The main idea is to count all the occurring characters in a string. If you
# have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then result should be empty object literal, {}.


def count(s):
    dict = {}
    if not s:
        return dict
    for letter in s:
        if letter not in dict:
            dict[letter] = 0
        dict[letter] += 1
    return dict


def count2(string):
    return {i: string.count(i) for i in string}
