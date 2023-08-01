# I will give you an integer. Give me back a shape that is as long and wide as
# the integer. The integer will be a whole number between 1 and 50.

# Example
# n = 3, so I expect a 3x3 square back just like below as a string:

# +++
# +++
# +++


def generate_shape(n):
    res = "+" * n
    full_line = (res) + "\n"
    return full_line * (n - 1) + res


def generateShape1(integer):
    return "\n".join("+" * integer for i in range(integer))
