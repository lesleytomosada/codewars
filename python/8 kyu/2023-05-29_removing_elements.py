#  https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

# Take an array and remove every second element from the array. Always keep
# the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", ...] --> ["Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that


def remove_every_other(my_list):
    return [my_list[i] for i in range(0, len(my_list), 2)]


def remove_every_other2(my_list):
    return my_list[::2]
