# Modify the kebabize function so that it converts a camel case string into a
# kebab case.

# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"
# Notes:

# the returned string should only contain lowercase letters


def kebabize(st):
    res = ""
    for i in range(len(st)):
        if st[i].isupper():
            res += f" {st[i].lower()}"
        elif st[i].islower():
            res += st[i]
    res = res.split()
    return "-".join(res)
