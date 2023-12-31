# ROT13 is a simple letter substitution cipher that replaces a letter with the
# letter 13 letters after it in the alphabet. ROT13 is an example of the
# Caesar cipher.

# Create a function that takes a string and returns the string ciphered with
# Rot13. If there are numbers or special characters included in the string,
# they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.


def rot13(message):
    output = ""

    for letter in message:
        if letter.isalpha():
            num = ord(letter.lower()) + 13
            if num > 122:
                num -= 26
            if letter.isupper():
                output += chr(num).upper()
            else:
                output += chr(num)

        else:
            output += letter

    return output


def rot13_2(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[
                (alpha.lower().index(letter) + 13) % 26
            ].lower()  # noqa
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) + 13) % 26]
        else:
            outputMessage += letter
    return outputMessage
