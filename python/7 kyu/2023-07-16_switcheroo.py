# Given a string made up of letters a, b, and/or c, switch the position of
# letters a and b (change a to b and vice versa). Leave any incidence of c
# untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'


def switcheroo(s):
    res = ""
    for c in s:
        if c == "a":
            res += "b"
        elif c == "b":
            res += "a"
        else:
            res += c
    return res
