# Assume "#" is like a backspace in string. This means that string "a#bc#d"
# actually is "bd"

# Your task is to process a string with "#" symbols.

# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""
# FUNDAMENTALSSTRINGSALGORITHMS
# Suggest kata description edits


def clean_string(s):
    stack = []
    for c in s:
        if c == "#":
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
