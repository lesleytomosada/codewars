def adjacent_element_product(array):
    prod = -float("inf")
    for i in range(len(array) - 1):
        prod = max(prod, array[i] * array[i + 1])
    return prod


def adjacent_element_product1(array):
    return max(a * b for a, b in zip(array, array[1:]))
