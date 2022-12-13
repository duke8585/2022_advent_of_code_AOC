from pprint import pprint as p


aoc_10 = open("./AOC_door_10.txt", "r").read().splitlines()
aoc_10 = aoc_10  # + ["noop"] * 10

# cycles = 0


# def parse_line(line, cycles, x):
#     match line.split(" "):
#         case ["noop"]:
#             x += 1
#             cycles += 1
#         case ["addx", modifier]:
#             print(modifier)
#             x = eval(f"x + {modifier}")
#             cycles += 3
#         case _:
#             raise ValueError("something wrong")
#     return cycles, x


# # cycles, x = parse_line("addx -14", cycles, x)

# aoc_10 = (
#     """noop
# addx 3
# addx -5""".splitlines()
#     + ["noop"] * 3
# )


def v1():

    x = 1
    l = []
    operations_queue = [0]
    signal_values = {}
    aoc_10_1 = aoc_10[:25]  # + ["noop"] * 100

    for n, line in enumerate(aoc_10_1):
        cycle = n + 1
        next_operation = operations_queue.pop(0)
        computation = f"x + {next_operation}"
        match line.split(" "):
            case ["noop"]:
                operations_queue.append(0)
            case ["addx", modifier]:
                operations_queue.append(0)
                operations_queue.append(modifier)
            case _:
                raise ValueError("something wrong")
        print(
            f"during cycle: {cycle}, x: {x}, computation: {computation}, operations-queue: {operations_queue}, signal-strength: {cycle*x}"
        )

        if cycle in range(20, 500, 40):
            signal_values[cycle] = cycle * x

        x = eval(computation)

        # next_operation = operations.pop(0)
        # x = eval(f"x + {next_operation}")

    print(signal_values)
    print(sum(signal_values.values()))


# v1()

# almost working


##
##


def v2():
    aoc_10_2 = aoc_10  # [:20]  # + [0] * 100
    cycle = 0
    x = 1
    done = False
    signal = []
    computation = "x + 0"

    def inc_cycle():
        nonlocal x, cycle, signal
        cycle += 1

        if cycle in range(20, 500, 40):
            signal.append(cycle * x)

    while not done:
        operation = aoc_10_2.pop()

        match operation.split(" "):
            case ["noop"]:
                inc_cycle()
            case ["addx", modifier]:
                inc_cycle()
                inc_cycle()
                computation = f"x + {modifier}"
                x = eval(computation)
            case _:
                raise ValueError("something wrong")

        done = len(aoc_10_2) == 0
        print(
            f"during cycle: {cycle}, x: {x}, computation: {computation}, signal-strength: {(cycle)*x}"
        )


# does not work :(
# v2()


#
# from subreddit solutions and adapted


def vreddit():
    #!/usr/bin/env python

    instructions = aoc_10

    x = 1
    cycle = 0
    signal = list()

    def increment_cycle():
        nonlocal x, cycle, signal

        cycle += 1

        print(f"cycle {cycle}, ins: {ins}, x {x}")

        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal.append(cycle * x)

    for ins in instructions:
        match ins.split(" "):
            case ["noop"]:
                increment_cycle()
            case ["addx", modifier]:
                increment_cycle()
                increment_cycle()
                x += int(modifier)

    print(sum(signal))


vreddit()


def vreddit_p2():
    instructions = aoc_10

    x = 1
    cycle = 0

    def increment_cycle():
        nonlocal x, cycle

        if (cycle + 1) % 40 == 0:
            print("\n", end="")
        elif cycle % 40 == x or cycle % 40 == x - 1 or cycle % 40 == x + 1:
            print("⬛️", end="")
        else:
            print("⬜️", end="")

        cycle += 1

    for ins in instructions:
        match ins.split(" "):
            case ["noop"]:
                increment_cycle()
            case ["addx", modifier]:
                increment_cycle()
                increment_cycle()
                x += int(modifier)


vreddit_p2()
