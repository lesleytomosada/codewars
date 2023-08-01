# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher
# this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"


def encrypt_this(text):
    res = []
    words = text.split()
    for word in words:
        encrypted = str(ord(word[0]))
        if len(word) > 2:
            new_word = encrypted + word[-1] + word[2:-1] + word[1]
        elif len(word) == 1:
            new_word = encrypted
        elif len(word) == 2:
            new_word = encrypted + word[1]
        res.append(new_word)

    return " ".join(res)


def encrypt_this2(text):
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append("".join(word))

    return " ".join(result)
