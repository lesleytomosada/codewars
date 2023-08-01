# In this kata, you will write a function that returns the positions and the
# values of the "peaks" (or local maxima) of a numeric array.

# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3
# with a value of 5 (since arr[3] equals 5).

# The output will be returned as an object with two properties: pos and peaks.
#  Both of these properties should be arrays. If there is no peak in the given
#  array, then the output should be {pos: [], peaks: []}.

# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos:
# [3, 7], peaks: [6, 3]} (or equivalent in other languages)

# All input arrays will be valid integer arrays (although it could still be
#  empty), so you won't need to validate the input.

# The first and last elements of the array will not be considered as peaks (in
#  the context of a mathematical function, we don't know what is after and
#  before and therefore, we don't know if it is a peak or not).

# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3]
#  and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return
# the position and value of the beginning of the plateau. For example:
# pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in
#  other languages)

# Have fun!


def pick_peaks(arr):
    result = {"pos": [], "peaks": []}

    differences = [0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            differences.append("+")
        elif arr[i] < arr[i - 1]:
            differences.append("-")
        else:
            differences.append("0")

    plateau = None
    plateau_peak = 0
    plateau_pos = 0

    for i in range(1, len(differences)):
        if differences[i] == "-" and differences[i - 1] == "+":
            result["pos"].append(i - 1)
            result["peaks"].append(arr[i - 1])
        elif differences[i] == "0" and differences[i - 1] == "+":
            plateau = True
            plateau_peak = arr[i - 1]
            plateau_pos = i - 1
        elif (
            plateau is True
            and differences[i] == "-"
            and differences[i - 1] == "0"  # noqa
        ):  # noqa
            plateau = None
            result["pos"].append(plateau_pos)
            result["peaks"].append(plateau_peak)
    return result


def pick_peaks2(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prob_peak = i
        elif arr[i] < arr[i - 1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {"pos": pos, "peaks": [arr[i] for i in pos]}
