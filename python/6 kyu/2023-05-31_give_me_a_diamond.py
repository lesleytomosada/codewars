# DESCRIPTION:
# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants
#  a diamond string from James. Since James doesn't know how to make this
# happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when printed on
# the screen, using asterisk (*) characters. Trailing spaces should be removed,
# and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is
# not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *
# ...that is:

# "  *\n ***\n*****\n ***\n  *\n"


def diamond(n):
    # Make some diamonds!
    diamond = ""
    if n <= 0 or n % 2 == 0:
        return None

    for i in range((n // 2 + 1)):
        multiplier = (2 * int(i)) - 1
        stars = "*" * multiplier
        spaces = " " * ((int(n) - len(stars)) // 2)
        if multiplier >= 1:
            line = f"{spaces}{stars}\n"
            diamond += line

    for i in range(n // 2 + 1, -1, -1):
        multiplier = (2 * int(i)) - 1
        stars = "*" * multiplier
        spaces = " " * ((int(n) - len(stars)) // 2)
        if multiplier >= 1:
            line = f"{spaces}{stars}\n"
            diamond += line

    return diamond


def diamond2(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n / 2) - i)
            diamond += "*" * (n - abs((n - 1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None


def diamond3(n):
    if n < 0 or n % 2 == 0:
        return None
    # result = the center line
    result = "*" * n + "\n"
    spaces = 1
    n = n - 2

    # start from the center line, then work outwards
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current

    return result
