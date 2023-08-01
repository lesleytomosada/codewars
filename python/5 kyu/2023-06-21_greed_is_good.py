# Greed is a dice game played with five six-sided dice. Your mission, should
# you choose to accept it, is to score a throw according to these rules. You
# will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5"
# can only count as part of a triplet (contributing to the 500 points) or as a
# single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function. This
# is something that you should never do. If you mutate the input, you will not
# be able to pass all the tests.


def score(dice):
    score = 0
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for num in dice:
        dict[num] += 1

    for _ in range(len(dice)):
        if dict[1] >= 3:
            score += 1000
            dict[1] -= 3
        if dict[6] >= 3:
            score += 600
            dict[6] -= 3
        if dict[5] >= 3:
            score += 500
            dict[5] -= 3
        if dict[4] >= 3:
            score += 400
            dict[4] -= 3
        if dict[3] >= 3:
            score += 300
            dict[3] -= 3
        if dict[2] >= 3:
            dict[2] -= 3
            score += 200
        if 3 > dict[1] >= 1:
            dict[1] -= 1
            score += 100
        if 3 > dict[5] >= 1:
            dict[5] -= 1
            score += 50

    return score


def score2(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for i, count in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum
