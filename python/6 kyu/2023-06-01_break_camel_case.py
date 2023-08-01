# DESCRIPTION:
# Complete the solution so that the function will break up camel casing, using
# a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    i = 0
    while i < len(s):
        if s[i].isupper():
            s = s[:i] + " " + s[i:]
            i += 2
        i += 1
    return s


def solution2(s):
    return "".join(" " + c if c.isupper() else c for c in s)
