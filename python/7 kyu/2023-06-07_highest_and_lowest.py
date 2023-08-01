def high_and_low(numbers):
    num_list = numbers.split()
    high, low = int(num_list[0]), int(num_list[0])
    for num in num_list:
        if int(num) > high:
            high = int(num)
        elif int(num) < low:
            low = int(num)
    return f"{high} {low}"


def high_and_low2(numbers):
    numbers = [int(c) for c in numbers.split(" ")]
    return f"{max(numbers)} {min(numbers)}"
