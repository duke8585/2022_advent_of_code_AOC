# AOC door_2

aoc_2_file = open("./AOC_door_2.txt", "r").read().splitlines()  # [:4]
aoc_2 = [l.split(" ") for l in aoc_2_file]
print(aoc_2[:5])


def result(me, op):
    # draws
    if me == "X" and op == "A":
        my_scores.append(1 + 3)
    if me == "Y" and op == "B":
        my_scores.append(2 + 3)
    if me == "Z" and op == "C":
        my_scores.append(3 + 3)
    # non-draws
    if me == "X" and op == "C":  # i win
        my_scores.append(1 + 6)
    if me == "Y" and op == "A":  # i win
        my_scores.append(2 + 6)
    if me == "Z" and op == "B":  # i win
        my_scores.append(3 + 6)
    if me == "Z" and op == "A":  # op wins
        my_scores.append(3 + 0)
    if me == "X" and op == "B":  # op wins
        my_scores.append(1 + 0)
    if me == "Y" and op == "C":  # op wins
        my_scores.append(2 + 0)


def move_to_make(op, result):
    if result == "X":  # need lose
        if op == "A":
            return "Z"
        if op == "B":
            return "X"
        if op == "C":
            return "Y"
    if result == "Y":  # need draw
        if op == "A":
            return "X"
        if op == "B":
            return "Y"
        if op == "C":
            return "Z"
    if result == "Z":  # need win
        if op == "A":
            return "Y"
        if op == "B":
            return "Z"
        if op == "C":
            return "X"


# result("X", "B")  # lose
# result("X", "C")  # win
# result("X", "A")  # draw rock
# result("Y", "B")  # draw rock
# ### result [2, 7, 4, 5]


my_scores = []

for choices in aoc_2:
    op = choices[0]
    me = choices[1]
    result(me=me, op=op)

print("===P1===")
print(my_scores)
print(sum(my_scores))

###
###

my_scores = []

for choices in aoc_2:
    op = choices[0]
    expected_result = choices[1]
    me = move_to_make(op, expected_result)
    result(me=me, op=op)

print("===P1===")
print(my_scores)
print(sum(my_scores))

###
###

# rock A
# paper B
# scissors C

lose_against = {"A": "C", "B": "A", "C": "B"}
win_against = {v: k for k, v in lose.items()}
draw = {k: k for k, v in lose.items()}
