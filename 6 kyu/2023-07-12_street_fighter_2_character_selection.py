# Test

# For this easy version the fighters grid layout and the initial position will
# always be the same in all tests, only the list of moves change.

# Notice: changing some of the input data might not help you.

# Examples

# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['up', 'left', 'right', 'left', 'left']
# then I should get:

# ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']
# as the characters I've been hovering with the selection cursor during my
# moves. Notice: Ryu is the first just because it "fails" the first up See
# test cases for more examples.

# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']
# Result:

# ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']


def street_fighter_selection(fighters, initial_position, moves):
    res = []
    x, y = initial_position
    for move in moves:
        if move == "up":
            x = 0
        elif move == "down":
            x = 1
        elif move == "right":
            y += 1
            if y > 5:
                y = 0
        elif move == "left":
            y -= 1
            if y == -1:
                y = 5

        res.append(fighters[x][y])
    return res


MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}


def street_fighter_selection2(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters
