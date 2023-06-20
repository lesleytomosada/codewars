# DESCRIPTION:
# Your task, is to create N×N multiplication table, of size provided in
# parameter.

# For example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:

# [[1,2,3],[2,4,6],[3,6,9]]


def multiplication_table(size):
    matrix = []
    first_row = []
    for i in range(1, size + 1):
        first_row.append(i)
    matrix.append(first_row)

    for i in range(2, size + 1):
        row = [i * n for n in first_row]
        matrix.append(row)

    return matrix


def multiplication_table2(size):
    columns = []
    for i in range(1, size + 1):
        rows = []
        for j in range(1, size + 1):
            rows.append(i * j)
        columns.append(rows)

    return columns
