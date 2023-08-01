# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function
# represents the right operand
# Division should be integer division. For example, this should return 2, not
# 2.666666...:
# eight(divided_by(three()))


def zero(arg=""):
    return eval("0" + arg)


def one(arg=""):
    return eval("1" + arg)


def two(arg=""):
    return eval("2" + arg)


def three(arg=""):
    return eval("3" + arg)


def four(arg=""):
    return eval("4" + arg)


def five(arg=""):
    return eval("5" + arg)


def six(arg=""):
    return eval("6" + arg)


def seven(arg=""):
    return eval("7" + arg)


def eight(arg=""):
    return eval("8" + arg)


def nine(arg=""):
    return eval("9" + arg)


def plus(n):
    return "+" + str(n)


def minus(n):
    return "-" + str(n)


def times(n):
    return "*" + str(n)


def divided_by(n):
    return "//" + str(n)
