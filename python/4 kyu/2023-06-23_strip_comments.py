# Complete the solution so that it strips all text that follows any of a set
# of comment markers passed in. Any whitespace at the end of the line should
# also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples",
# ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


def strip_comments(strng, markers):
    res = []
    lines = strng.split("\n")
    for line in lines:
        for marker in markers:
            if marker in line:
                new_list = line.split(marker)
                line = new_list[0].rstrip()
        res.append(line)
    return "\n".join(res)


def solution2(string, markers):
    parts = string.split("\n")
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return "\n".join(parts)
