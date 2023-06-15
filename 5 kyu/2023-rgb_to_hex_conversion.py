# The rgb function is incomplete. Complete it so that passing in RGB decimal
# values will result in a hexadecimal representation being returned. Valid
# decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3
# will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    res = []
    colors = [r, g, b]
    letter_conversion = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for color in colors:
        if color < 0:
            res.append("00")
        elif color > 255:
            res.append("FF")
        else:
            hex_1 = color // 16
            if hex_1 > 9:
                hex_1 = letter_conversion[hex_1]
            res.append(str(hex_1))
            hex_2 = color % 16
            if hex_2 > 9:
                hex_2 = letter_conversion[hex_2]
            res.append(str(hex_2))
    return "".join(res)


def hex_con(color):
    hex_dict = "0123456789ABCDEF"
    d1 = color // 16
    d2 = color % 16
    if d1 > 15:
        d1 = 15
        d2 = 15
    elif d1 < 0:
        d1 = 0
        d2 = 0
    return str(hex_dict[d1]) + str(hex_dict[d2])


def rgb2(r, g, b):
    R = hex_con(r)
    G = hex_con(g)
    B = hex_con(b)
    return R + G + B
