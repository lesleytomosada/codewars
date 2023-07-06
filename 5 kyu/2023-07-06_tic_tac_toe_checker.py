# If we were to set up a Tic-Tac-Toe game, we would want to know whether the
# board's current state is solved, wouldn't we? Our goal is to create a
# function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0
# if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty
# spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of
# Tic-Tac-Toe.


def is_solved(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]

    columns = []

    for i in range(3):
        column = []
        for j in range(3):
            column.append(board[j][i])
        columns.append(column)

    for column in columns:
        if column[0] == column[1] == column[2] and column[0] != 0:
            return column[0]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    for row in board:
        if 0 in row:
            return -1

    return 0
