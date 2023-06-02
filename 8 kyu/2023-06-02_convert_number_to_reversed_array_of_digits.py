# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this
# number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


def digitize(n):
    output = []
    for num in str(n):
        output.insert(0, int(num))
    return output


def digitize2(n):
    return [int(num) for num in str(n)[::-1]]
