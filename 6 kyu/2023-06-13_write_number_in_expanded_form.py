# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in
# Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!


def expanded_form(num):
    res = []
    length = len(str(num))
    for i in range(length):
        new_num = str(num)[i] + ("0" * (length - 1 - i))
        if int(new_num) > 0:
            res.append(new_num)
    return " + ".join(res)


def expanded_form2(num):
    num = list(str(num))
    return " + ".join(
        x + "0" * (len(num) - y - 1) for y, x in enumerate(num) if x != "0"
    )
