from pprint import pprint as p
import re

aoc_5 = open("./AOC_door_5.txt", "r").read().splitlines()
aoc_5 = aoc_5[10:]
# aoc_5 = aoc_5[:3]

"""
[B]                     [N]     [H]
[V]         [P] [T]     [V]     [P]
[W]     [C] [T] [S]     [H]     [N]
[T]     [J] [Z] [M] [N] [F]     [L]
[Q]     [W] [N] [J] [T] [Q] [R] [B]
[N] [B] [Q] [R] [V] [F] [D] [F] [M]
[H] [W] [S] [J] [P] [W] [L] [P] [S]
[D] [D] [T] [F] [G] [B] [B] [H] [Z]
 1   2   3   4   5   6   7   8   9
 """

stacks = [
    ["XXX"],  # 0 so easier
    ["D", "H", "N", "Q", "T", "W", "V", "B"],  # 1
    ["D", "W", "B"],  # 2
    ["T", "S", "Q", "W", "J", "C"],  # 3
    ["F", "J", "R", "N", "Z", "T", "P"],  # 4
    ["G", "P", "V", "J", "M", "S", "T"],  # 5
    ["B", "W", "F", "T", "N"],  # 6
    ["B", "L", "D", "Q", "F", "H", "V", "N"],  # 7
    ["H", "P", "F", "R"],  # 8
    ["Z", "S", "M", "B", "L", "N", "P", "H"],  # 9
]


def show_stacks(stacks):
    print("-----------------------------")
    for n, stack in enumerate(stacks):
        print(f"{n} | {stack}")
    print("-----------------------------")


def take_stack(stack_from, amount):
    """take a list stack and remove a load"""
    stack_from.reverse()
    removed = stack_from[0:amount]
    if CrateMover9001:
        removed.reverse()  # part 2
    del stack_from[0:amount]
    stack_from.reverse()
    return stack_from, removed


def put_stack(stack_to, load):
    stack_to += load
    return stack_to


show_stacks(stacks)
print("========================")

CrateMover9001 = True

for n, change in enumerate(aoc_5):
    print(f"cycle {n+1}: {change}")
    amount, stack_from, stack_to = [int(x) for x in re.findall("(\d+)", change)]
    # print(amount, stack_from, stack_to)
    # removing part
    stack_from_old = stacks[stack_from]
    stack_from_new, load = take_stack(stack_from_old, amount)
    stacks[stack_from] = stack_from_new
    # placing part
    stack_to_old = stacks[stack_to]
    stack_to_new = put_stack(stack_to_old, load)
    stacks[stack_to] = stack_to_new
    show_stacks(stacks)

print("========================")
show_stacks(stacks)
