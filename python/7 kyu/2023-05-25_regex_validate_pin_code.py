# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/python

# DESCRIPTION:
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
# anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false


def validate_pin(pin):
    nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    if len(pin) > 6 or len(pin) == 5 or len(pin) < 4:
        return False
    for num in pin:
        if num not in nums:
            return False
    return True


# best practice
def validate_pin2(pin):
    return len(pin) in [4, 6] and pin.isdigit()
