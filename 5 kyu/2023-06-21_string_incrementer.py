# Your job is to write a function which increments a string, to create a new
# string.

# If the string already ends with a number, the number should be incremented
# by 1.
# If the string does not end with a number. the number 1 should be appended to
# the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be
# considered.


def increment_string(string):
    print(string)
    if not string:
        return "1"
    if string[-1].isalpha():
        string += "1"
    else:
        if len(string) > 1:
            i = 1
            count = 0
            while string[-i].isnumeric() and i < len(string):
                count += 1
                i += 1
            first_half = string[: len(string) - count]
            second_half = string[len(string) - count :]  # noqa
            num_length = len(second_half)
            num_increment = int(second_half) + 1
            zeroes = num_length - len(str(num_increment))
            if zeroes == 0:
                string = first_half + str(num_increment)
            else:
                string = first_half + ("0" * zeroes) + str(num_increment)
        else:
            if string.isnumeric():
                return str(int(string) + 1)
            else:
                return string + "1"
    return string


def increment_string2(strng):
    head = strng.rstrip("0123456789")
    tail = strng[len(head) :]  # noqa
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
