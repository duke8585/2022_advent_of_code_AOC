aoc_3 = open("./AOC_door_3.txt", "r").read().splitlines()
# aoc_3 = aoc_3[:5]

lower_ascii = "abcdefghijklmnopqrstuvwxyz"
lower = {v: i + 1 for i, v in enumerate(lower_ascii)}
upper = {v: i + 27 for i, v in enumerate(lower_ascii.upper())}
lookup = lower | upper


def ordinal_number(s):
    return lookup.get(s)


commons = []

backpacks = aoc_3

for backpack in backpacks:
    l = len(backpack)
    # fixed = sorted(backpack, key=lambda x: ordinal_number(x))
    # print(fixed)
    # fixed = "".join(fixed)
    one = backpack[: l // 2]
    two = backpack[l // 2 :]
    common = set(one).intersection(set(two))
    commons.append(list(common)[0])
    # print(backpack, one, two, common)

common_prios = list(map(ordinal_number, commons))
print(sum(common_prios))

###
### part 2
###

elve_squads = [backpacks[i : i + 3] for i in range(0, len(backpacks), 3)]

common_in_squads = [list(set(s[0]) & set(s[1]) & set(s[2]))[0] for s in elve_squads]

common_in_squads_prios = list(map(ordinal_number, common_in_squads))

print(sum(common_in_squads_prios))
