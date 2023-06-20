# Complete the function scramble(str1, str2) that returns true if a portion of
# str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be
# included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1, s2):
    dict = {}

    for c in s1:
        if c not in dict:
            dict[c] = 0
        dict[c] += 1

    for c in s2:
        if c not in dict:
            return False
        if dict[c] == 0:
            return False
        dict[c] -= 1

    return True
