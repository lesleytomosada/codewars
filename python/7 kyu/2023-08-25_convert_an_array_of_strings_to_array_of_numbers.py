# Oh no!
# Some really funny web dev gave you a sequence of numbers from his API
# response as an sequence of strings!

# You need to cast the whole array to the correct type.

# Create the function that takes as a parameter a sequence of numbers
# represented as strings and outputs a sequence of numbers.

# ie:["1", "2", "3"] to [1, 2, 3]

# Note that you can receive floats as well.


def to_float_array(arr):
    res = []
    for num in arr:
        if len(num) > 1:
            res.append(float(num))
        else:
            res.append(int(num))
    return res


def to_float_array2(arr):
    return list(map(float, arr))
