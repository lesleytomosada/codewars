# DESCRIPTION:
# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same value next
# to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


def unique_in_order(sequence):
    if not sequence:
        return []

    output = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i - 1] != sequence[i]:
            output.append(sequence[i])

    return output


def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
