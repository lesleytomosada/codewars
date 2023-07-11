# Complete the function/method so that it takes a PascalCase string and
# returns the string in snake_case notation. Lowercase characters can be
# numbers. If the method gets a number as input, it should return a string.

# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"


def to_underscore(string):
    res = ""
    string = str(string)
    for c in string:
        if c.isdigit():
            res += str(c)
        elif c.isupper():
            res += " "
            res += c.lower()
        elif c.islower():
            res += c
    res = res.strip()
    return res.replace(" ", "_")


def to_underscore2(string):
    string = str(string)
    new = []
    for s in string:
        if not new:
            new.append(s)
        else:
            if s.isupper():
                new.append("_")
            new.append(s)
    return "".join(new).lower()
