# AOC door_1

test = [100, 120, 130, "", 150, "", 180, 120, "", 290, 450, 550, "", 200, 300, 310, 320]
aoc_1 = open("./AOC_door_1.txt", "r").read().splitlines()

elve_number = 1
cal_sum = 0
elves_cals = {}

for cal_item in aoc_1:
    if len(cal_item) > 0:
        cal_sum += int(cal_item)
    else:
        elves_cals[elve_number] = cal_sum
        cal_sum = 0
        elve_number += 1

print(sorted(elves_cals.items(), key=lambda x: x[1]))
