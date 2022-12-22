from pprint import pprint as p


#               __ _       _     _              _
#              / _(_)     (_)   | |            | |
#  _   _ _ __ | |_ _ _ __  _ ___| |__   ___  __| |
# | | | | '_ \|  _| | '_ \| / __| '_ \ / _ \/ _` |
# | |_| | | | | | | | | | | \__ \ | | |  __/ (_| |
#  \__,_|_| |_|_| |_|_| |_|_|___/_| |_|\___|\__,_|


aoc_21 = open("./AOC_door_21.txt", "r").read().splitlines()
aoc_21 = aoc_21  # + ["noop"] * 10

# print(aoc_21)

test = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip().splitlines()

print(test)
monkeys = {}

for line in test:
    key, val = (e.strip() for e in line.split(":"))
    monkeys.update({key: val})

print(monkeys)


def monkey_shouts(mon_key):
    """
    find the monkey in the monkey dict:
    * if single value, return
    * if operation, return eval with recursion
    """
    mon_val = monkeys.get(mon_key)
    match mon_val.split(" "):
        case [number]:
            return number
        case [mon_1, op, mon_2]:
            behind_mon_1 = monkey_shouts(mon_1)
            behind_mon_2 = monkey_shouts(mon_2)
            return eval(f"{behind_mon_1}{op}{behind_mon_2}")


print(f"""test: {monkey_shouts("root")}""")

monkeys = {}

for line in aoc_21:
    key, val = (e.strip() for e in line.split(":"))
    monkeys.update({key: val})

print(f"""part 1: {monkey_shouts("root")}""")

##
## part 2
##

# root: wrvq + vqfc

print(" part 2 " * 10)

print(f"""wrvq : {monkey_shouts("wrvq")}""")
print(f"""vqfc : {monkey_shouts("vqfc")}""")

# humn: 1117 initial
vqfc = monkey_shouts("vqfc")  # not dependent on humn

# between 3732000000000 and 3742000000000
# always look for boundaries around the minumum ...
begin, end = 3715799488096, 3715799488160
stepsize = (end - begin) // 10

for me in range(begin, end, stepsize):
    monkeys.update({"humn": str(me)})
    wrvq = monkey_shouts("wrvq")
    # print(f"me: {me}, wrvq: {wrvq}, vqfc: {vqfc}")
    print(f"me: {me}, wrvq-vqfc: {abs(wrvq-vqfc)}")
    if vqfc == wrvq:
        print(f"!!! humn MUST BE {me}")
        break
