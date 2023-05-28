# DESCRIPTION:
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in
# the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def duplicate_count(text):
    dict = {}
    for letter in text:
        lower = letter.lower()
        if lower not in dict:
            dict[lower] = 0
        dict[lower] += 1

    output = []
    for key in dict.keys():
        if dict[key] > 1:
            output.append(key)

    return len(output)


# best practice


def duplicate_count2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
