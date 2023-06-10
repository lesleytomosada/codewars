# Move the first letter of each word to the end of it, then add "ay" to the
# end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    output = ""
    for word in text.split():
        if word.isalpha():
            output += f"{word[1:]}{word[0]}ay "
        else:
            output += word
    return output.strip()


def pig_it2(text):
    lst = text.split()
    return " ".join(
        [word[1:] + word[:1] + "ay" if word.isalpha() else word for word in lst]  # noqa
    )
