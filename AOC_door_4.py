aoc_4 = open("./AOC_door_4.txt", "r").read().splitlines()
# aoc_4 = aoc_3[:5]

print(aoc_4)

fully_contains = []
partial_overlap = []
disjoint = []


def set_from_range(rng):
    bounds = rng.split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])
    # print(bounds, lower, upper, type(lower))
    range_set = set(range(lower, upper + 1))
    return range_set


for ranges in aoc_4:
    range_1, range_2 = ranges.split(",")
    set_1 = set_from_range(range_1)
    set_2 = set_from_range(range_2)
    overlap = set_1.intersection(set_2)
    overlap_len = len(overlap)
    smaller_set_len = min(len(set_1), len(set_2))
    if overlap_len == smaller_set_len:
        fully_contains.append(ranges)
    if overlap_len > 0:
        partial_overlap.append(ranges)
    else:
        disjoint.append(ranges)

print(len(fully_contains), fully_contains[:5])
print(len(partial_overlap), fully_contains[:5])
print(len(disjoint), disjoint[:5])
