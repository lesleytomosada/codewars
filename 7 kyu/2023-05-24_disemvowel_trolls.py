# https://www.codewars.com/kata/52fba66badcd10859f00097e/python

# DESCRIPTION:
# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from
# the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string
# with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths
# wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    no_a = string.replace('a', '')
    no_e = no_a.replace('e', '')
    no_i = no_e.replace('i', '')
    no_o = no_i.replace('o', '')
    no_u = no_o.replace('u', '')
    no_A = no_u.replace('A', '')
    no_E = no_A.replace('E', '')
    no_I = no_E.replace('I', '')
    no_O = no_I.replace('O', '')
    no_U = no_O.replace('U', '')
    return no_U


# better solution
def disemvowel2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s
