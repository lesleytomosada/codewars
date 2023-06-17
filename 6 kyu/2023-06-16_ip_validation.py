# Write an algorithm that will identify valid IPv4 addresses in dot-decimal
# format. IPs should be considered valid if they consist of four octets, with
# values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string


def is_valid_IP(strng):
    nums = strng.split(".")
    if len(nums) != 4:
        return False
    for num in nums:
        try:
            if int(num) < 0 or int(num) > 255:
                return False
            if len(num) > 1 and num[0] == "0":
                return False
            if " " in num:
                return False
            if "\n" in num:
                return False
        except ValueError:
            return False

    return True


def is_valid_IP2(strng):
    nums = strng.split(".")
    if len(nums) != 4:
        return False
    digit_range = set()
    for i in range(256):
        digit_range.add(str(i))
    for num in nums:
        try:
            if num not in digit_range:
                return False
        except ValueError:
            return False
    return True


def is_valid_IP3(strng):
    if len(strng.split(".")) != 4:
        return False

    for group in strng.split("."):
        if (
            not group.isdigit()
            or group != str(int(group))
            or not 0 <= int(group) <= 255
        ):
            return False

    return True
