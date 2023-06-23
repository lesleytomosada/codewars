# DESCRIPTION:
# In this example you have to validate if a user input string is alphanumeric.
# The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0
# to 9
# No whitespaces / underscore


def alphanumeric(password):
    if " " in password or "_" in password or not password:
        return False
    for c in password:
        if not c.isalnum():
            return False
    return True


def alphanumeric2(string):
    return string.isalnum()
