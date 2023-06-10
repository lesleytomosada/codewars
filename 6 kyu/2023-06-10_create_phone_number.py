# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns
# "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!


def create_phone_number(n):
    res = "("
    for i in range(3):
        res += str(n[i])
    res += ") "
    for i in range(3, 6):
        res += str(n[i])
    res += "-"
    for i in range(6, 10):
        res += str(n[i])

    return res


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
