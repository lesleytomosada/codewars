# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

# In this Kata, you will be given a string that may have mixed uppercase and
# lowercase letters and your task is to convert that string to either
# lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters,
# convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the
# "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the
# "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
# More examples in test cases. Good luck!


def solve(s):
    upper = 0
    lower = 0
    for letter in s:
        if letter.isupper():
            upper += 1
        else:
            lower += 1

    return s.lower() if upper <= lower else s.upper()


def solve2(s):
    lower_case = [lower for lower in s if lower.islower()]
    upper_case = [upper for upper in s if upper.isupper()]

    if len(upper_case) > len(lower_case):
        return s.upper()
    return s.lower()
