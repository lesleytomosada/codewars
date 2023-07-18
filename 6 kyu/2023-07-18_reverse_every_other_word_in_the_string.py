# Reverse every other word in a given string, then return the string. Throw
# away any leading or trailing whitespace, while ensuring there is exactly one
# space between each word. Punctuation marks should be treated as if they are
# a part of the word in this kata.

# ARRAYSFUNDAMENTALS


def reverse_alternate(s):
    words = s.split()

    for i in range(len(words)):
        if i % 2 != 0:
            words[i] = words[i][::-1]

    return " ".join(words)


def reverse_alternate1(string):
    return " ".join(
        y[::-1] if x % 2 else y for x, y in enumerate(string.split())
    )  # noqa
