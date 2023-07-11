# Johnny is a farmer and he annually holds a beet farmers convention "Drop the
# beet".

# Every year he takes photos of farmers handshaking. Johnny knows that no two
# farmers handshake more than once. He also knows that some of the possible
# handshake combinations may not happen.

# However, Johnny would like to know the minimal amount of people that
# participated this year just by counting all the handshakes.

# Help Johnny by writing a function, that takes the amount of handshakes and
# returns the minimal amount of people needed to perform these handshakes
# (a pair of farmers handshake only once).


def get_participants(handshakes):
    handshakes = int(handshakes)
    dict = {}
    running_total = 0
    for i in range(handshakes + 2):
        dict[i] = running_total
        running_total += i

    values = []
    keys = []
    for key, val in dict.items():
        values.append(val)
        keys.append(key)

    values.sort()
    keys.sort()

    for i in range(len(values)):
        if i == len(values) - 1:
            return keys[i]
        if values[i] < handshakes:
            continue
        elif values[i] >= handshakes:
            return keys[i]
        if i == len(values) - 1:
            return keys[i]
