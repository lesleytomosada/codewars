# Implement a pseudo-encryption algorithm which given a string S and an
# integer N concatenates all the odd-indexed characters of S with all the
# even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a
# decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return
# the first argument without changes.

# This kata is part of the Simple Encryption Series:


# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
# Have fun coding it and please don't forget to vote and rank this kata! :-)
def decrypt1(encrypted_text, n):
    res = encrypted_text

    for _ in range(n):
        half = len(encrypted_text) // 2
        if len(encrypted_text) % 2 == 0:
            odds = res[:half]
            evens = res[half:]
        else:
            odds = res[:half]
            evens = res[half:]

        new_string = ""
        for i in range(len(odds)):
            new_string += evens[i]
            new_string += odds[i]
        if len(encrypted_text) % 2 != 0:
            new_string += evens[-1]
        res = new_string
    return res


def encrypt1(text, n):
    res = text
    for _ in range(n):
        odds = ""
        evens = ""
        for i in range(len(res)):
            if i % 2 == 0:
                evens += res[i]
            else:
                odds += res[i]
        res = odds + evens

    return res


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i : i + 1] + a[i : i + 1] for i in range(ndx + 1))  # noqa
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
