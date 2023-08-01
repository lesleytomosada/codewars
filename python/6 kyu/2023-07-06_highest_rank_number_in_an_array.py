# Complete the method which returns the number which is most frequent in the
# given input array. If there is a tie for most frequent number, return the
# largest number among them.

# Note: no empty arrays will be given.

# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


def highest_rank(arr):
    most_freq = 0
    num = 0
    dict = {}
    for num in arr:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1

    for key, value in dict.items():
        if value > most_freq:
            num = key
            most_freq = value
        elif value == most_freq:
            if key > num:
                most_freq = value
                num = key

    return num


def highest_rank1(arr):
    return max(sorted(arr, reverse=True), key=arr.count)
