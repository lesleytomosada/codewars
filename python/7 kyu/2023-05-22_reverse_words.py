# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

# DESCRIPTION:
# Complete the function that accepts a string parameter, and
# reverses each word in the string. All spaces in the string
# should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
