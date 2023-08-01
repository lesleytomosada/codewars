# Complete the method/function so that it converts dash/underscore delimited
# words into camel casing. The first word within the output should be
# capitalized only if the original word was capitalized (known as Upper
# Camel Case, also often referred to as Pascal case). The next words should
# be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    same_dash = text.replace("_", "-")
    list = same_dash.split("-")
    output = list[0]
    for i in range(1, len(list)):
        capitalized = list[i].capitalize()
        output += capitalized
    return output


def to_camel_case2(text):
    removed = text.replace("-", " ").replace("_", " ").split()
    if len(removed) == 0:
        return ""
    return removed[0] + "".join([x.capitalize() for x in removed[1:]])
