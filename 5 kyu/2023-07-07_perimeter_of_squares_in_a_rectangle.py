# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3,
# 5, 8. It's easy to see that the sum of the perimeters of these squares is :
# 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

# Could you give the sum of the perimeters of all the squares in a rectangle
# when there are n + 1 squares disposed in the same manner as in the drawing:

# alternative text

# Hint:
# See Fibonacci sequence

# Ref:
# http://oeis.org/A000045

# The function perimeter has for parameter n where n + 1 is the number of
# squares (they are numbered from 0 to n) and returns the total perimeter of
# all the squares.

# perimeter(5)  should return 80
# perimeter(7)  should return 216


def perimeter(n):
    prev_side = 1
    current_side = 1
    peri = 4 * (prev_side + current_side)

    for i in range(2, n + 1):
        new_side = current_side + prev_side
        peri += 4 * new_side

        prev_side = current_side
        current_side = new_side

    return peri


def perimeter1(n):
    list = [1, 1]
    for i in range(1, n):
        list.append(list[i] + list[i - 1])
    perimeter = 4 * sum(list)
    return perimeter
