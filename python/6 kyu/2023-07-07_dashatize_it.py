# Given a variable n,

# If n is an integer, Return a string with dash'-'marks before and after each
# odd integer, but do not begin or end the string with a dash mark. If n is
# negative, then the negative sign should be removed.

# If n is not an integer, return the string "None".

# Ex:

# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'


def dashatize(n):
    if not n and n != 0:
        return "None"
    n = abs(n)
    res = []
    if not str(n).isdigit():
        return "None"
    for i in str(n):
        if int(i) % 2 != 0:
            if res:
                if res[-1] != "-":
                    res.append("-")
                    res.append(str(i))
                    res.append("-")
                elif res[-1] == "-":
                    res.append(str(i))
                    res.append("-")
            else:
                res.append(str(i))
                res.append("-")
        else:
            res.append(i)

    if res[-1] == "-":
        res.pop()

    return "".join(res)


def dashatize1(num):
    num_str = str(num)
    for i in ["1", "3", "5", "7", "9"]:
        num_str = num_str.replace(i, "-" + i + "-")
    return num_str.strip("-").replace("--", "-")
