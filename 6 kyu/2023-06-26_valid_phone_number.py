# Write a function that accepts a string, and returns true if it is in the
# form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid
# phone number.

# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# Examples:

# "(123) 456-7890"  => true
# "(1111)555 2345"  => false
# "(098) 123 4567"  => false
# REGULAR EXPRESSIONSALGORITHMS


def valid_phone_number(phone_number):
    dict = {0: "(", 4: ")", 5: " ", 9: "-"}
    nums = "0123456789"

    if len(phone_number) != 14:
        return False

    for i in range(len(phone_number)):
        if i in dict:
            if dict[i] != phone_number[i]:
                return False
        else:
            if phone_number[i] not in nums:
                return False

    return True


def validPhoneNumber2(phoneNumber):
    number = ""
    template = "(xxx) xxx-xxxx"
    for num in phoneNumber:
        if num.isdigit():
            number += "x"
        else:
            number += num

    return number == template
