# DESCRIPTION:
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the
# alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest
# in the original string.

# All letters will be lowercase and all inputs will be valid.


def high(x):
    alphabet = "0abcdefghijklmnopqrstuvwxyz"
    words = x.split()
    max_word_score = 0
    max_word = ""
    for word in words:
        score = 0
        for letter in word:
            score += alphabet.index(letter)
        if score > max_word_score:
            max_word_score = score
            max_word = word
    return max_word


def high2(x):
    words = x.split(" ")
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
