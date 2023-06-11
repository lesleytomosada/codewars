# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data
# types.


def find_short(s):
    s_list = s.split()
    shortest = len(s_list[0])
    for word in s_list:
        if len(word) < shortest:
            shortest = len(word)
    return shortest


def find_short2(s):
    return min(len(x) for x in s.split())
