# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    i = 0
    j = 1
    while i < len(lst) and j < len(lst):
        if lst[i] > 0:
            i += 1
            j += 1
        elif lst[i] == 0 and lst[j] > 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1
        else:
            j += 1

    return lst
