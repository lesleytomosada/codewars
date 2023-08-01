# When working with color values it can sometimes be useful to extract the
# individual red, green, and blue (RGB) component values for a color.
# Implement a function that meets these requirements:

# Accepts a case-insensitive hexadecimal color string as its parameter (ex.
#  "#FF9933" or "#ff9933")
# Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where
#  r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand form of
#  hexadecimal notation (ie "#FFF")

# Example
# "#FF9933" --> {r: 255, g: 153, b: 51}


def hex_string_to_RGB(hex_string):
    red = hex_string[1:3]
    blue = hex_string[3:5]
    green = hex_string[5:7]
    hexes = [red, blue, green]

    conversion = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    values = []
    for color in hexes:
        value = 0
        if color[0].isalpha():
            value += int(conversion[color[0].upper()]) * 16
        if color[1].isalpha():
            value += int(conversion[color[1].upper()])
        if color[0].isdigit():
            value += int(color[0]) * 16
        if color[1].isdigit():
            value += int(color[1])
        values.append(value)

    return {"r": values[0], "g": values[1], "b": values[2]}


def hex_string_to_RGB2(hex_string):
    # your code here
    r = int(hex_string[1:3], 16)
    g = int(hex_string[3:5], 16)
    b = int(hex_string[5:7], 16)

    return {"r": r, "g": g, "b": b}
