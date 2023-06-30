# Task
# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.

# [output] a string
# FUNDAMENTALS


def reverse_letter(string):
    return "".join(
        [
            string[x]
            for x in range(len(string) - 1, -1, -1)
            if string[x].isalpha()  # noqa
        ]
    )


def reverse_letter2(s):
    return "".join([i for i in s if i.isalpha()])[::-1]
