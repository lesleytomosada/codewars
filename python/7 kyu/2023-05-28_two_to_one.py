# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

# Take 2 strings s1 and s2 including only letters from a to z. Return a new
# sorted string, the longest possible, containing distinct letters - each
# taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(a1, a2):
    output = ""
    combined = a1 + a2
    for letter in combined:
        if letter not in output:
            output += letter
    sorted_string = sorted(output)
    return "".join(sorted_string)


def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))
