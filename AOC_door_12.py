from pprint import pprint as p


#               __ _       _     _              _
#              / _(_)     (_)   | |            | |
#  _   _ _ __ | |_ _ _ __  _ ___| |__   ___  __| |
# | | | | '_ \|  _| | '_ \| / __| '_ \ / _ \/ _` |
# | |_| | | | | | | | | | | \__ \ | | |  __/ (_| |
#  \__,_|_| |_|_| |_|_| |_|_|___/_| |_|\___|\__,_|


aoc_12 = open("./AOC_door_12.txt", "r").read().splitlines()
aoc_12 = aoc_12  # + ["noop"] * 10

test = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi\
"""

matrix = test.splitlines()

# print(test)


def around(row, col, debug=False):
    width = len(matrix[0])
    height = len(matrix)
    if debug:
        print(f"row: {row}, height: {height}, column: {col}, width: {width}")
    # L, R, U, D
    directions = {}
    if row == 0:  # top
        if col == 0:  # top left
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
        elif col == width:  # top right
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
        else:
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
    elif row + 1 == height:  # bottom
        if col == 0:  # bottom left
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
        if col == width:  # bottom right
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
        else:
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
    elif col == 0:  # left
        if row == 0:  # left top
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
        elif row == height:  # left bottom
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
        else:
            directions["right"] = [matrix[row][col + 1], [row, col + 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
    elif col + 1 == width:  # right
        if row == 0:  # right top
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]
        if row == height:  # right bottom
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
        else:
            directions["left"] = [matrix[row][col - 1], [row, col - 1]]
            directions["up"] = [matrix[row - 1][col], [row - 1, col]]
            directions["down"] = [matrix[row + 1][col], [row + 1, col]]

    else:
        directions["left"] = [matrix[row][col - 1], [row, col - 1]]
        directions["right"] = [matrix[row][col + 1], [row, col + 1]]
        directions["up"] = [matrix[row - 1][col], [row - 1, col]]
        directions["down"] = [matrix[row + 1][col], [row + 1, col]]

    return directions


def show(matrix):
    print("----------")
    for r in matrix:
        new_row = " ".join([c for c in r])
        print(new_row)
    print("----------")


def get(row, col):
    # TODO include bounds, return None if outside
    return matrix[row][col]


def allowed(char):
    import string

    bonus = ""
    lowercase = string.ascii_lowercase
    if char == "S":  # entry case
        allowed = ["a"]
    if char == "z":  # exit case
        bonus = ["E"]
    # TODO if z then E
    else:  # generating a list from begin until position + 1 more
        allowed = list({c: lowercase[: i + 2] for i, c in enumerate(lowercase)}[char])
    return allowed + bonus


def decide(options: dict, allowed: list):
    import random

    ## TODO options looks like this: {'right': ['a', [0, 1]], 'down': ['a', [1, 0]]}
    ## TODO comprehension has to be changed

    allowed_options = [[k, v[1]] for k, v in options.items() if v in allowed]
    if len(allowed_options) > 1:
        random.choice(allowed_options)  # a random choice
    else:
        return allowed_options[0]  # the only one


def choose(neighbors: dict, decision):
    pass


# print(around(1, 1, debug=True))
# print("1,0", around(1, 0))
# print("1,1", around(1, 1))
# print("0,5", around(0, 5))
# print("0,5", around(3, 7))
# print("0,5", around(4, 4))


# print(
#     f"current_value {get(0, 0)}, neighbors {around(0, 0)}, allowed_neighbors {allowed(get(0, 0))}"
# )

# TODO
# walk the thing, make decisions with directions, options and choose
#

current_char = get(0, 0)
current_options = around(0, 0)
current_allowed_destinations = allowed(get(0, 0))
print(current_char, current_options, current_allowed_destinations)
# current_decision = decide(around(0, 0), allowed(get(0, 0)))


# print(f"choice {decide(around(0,0),allowed(get(0, 0)))}")
# show(matrix)
