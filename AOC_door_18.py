from pprint import pprint as p
import numpy as np


aoc_18 = open("./AOC_door_18.txt", "r").read().splitlines()
aoc_18 = aoc_18  # + ["noop"] * 10

# print(aoc_21)

test = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".strip().splitlines()

# print(test)


def get_grid_dimensions(coords):
    x_max = 0
    y_max = 0
    z_max = 0
    for coord in coords:
        match coord.split(","):
            case [z, y, x]:
                z_max = max(z_max, int(z))
                y_max = max(y_max, int(y))
                x_max = max(x_max, int(x))

    return x_max, y_max, z_max


# x_max, y_max, z_max = get_grid_dimensions(test)

# print("max of z, y, x:", z_max, y_max, x_max)


# def make_empty_grid(z_max, y_max, x_max):
#     # make a grid which allows for 1 void spaces in every dimensions boundary
#     x_max += 2
#     y_max += 2
#     z_max += 2
#     return [[[0 for x in range(y_max)] for y in range(x_max)] for z in range(z_max)]


def make_empty_numpy_grid(z_max, y_max, x_max):
    """make a grid which allows for 1 void spaces in every dimensions boundary"""
    x_max += 2
    y_max += 2
    z_max += 2
    return np.zeros([z_max, x_max, y_max])


# grid = make_empty_numpy_grid(z_max, x_max, y_max)

# grid = make_empty_grid(x_max, y_max, z_max)

# print(grid)


def place_droplets(grid, coords):
    """coords starting at 1, so at the second of our by-2-enlarged grid"""
    for coord in coords:
        match coord.split(","):
            case [z, x, y]:
                x = int(x)
                y = int(y)
                z = int(z)
                grid[z][x][y] = 1
            case _:
                raise (ValueError, "cannot parse")
        # break  # TODO remove

    return grid


def sum_bonds(l, pattern=[1, 1]):
    return 2 * sum(
        [l[x : x + 2] == pattern for x, i in enumerate(l)]
    )  # one 1-1 patterns means 2 lost vacancies or 2 bonds


def test_sum_bonds():
    l = [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
    bonds = sum_bonds(l)
    print(bonds)


def iter_rows_sum_bonds(grid):
    bonds = 0
    for slice in grid:
        for row in slice:
            bonds += sum_bonds(list(row))  # convert to python list to be flat
    return bonds


def iter_sum_bonds_all_projections(grid):
    s = sum(
        [
            iter_rows_sum_bonds(grid),
            iter_rows_sum_bonds(np.rot90(grid, k=1, axes=(1, 2))),
            iter_rows_sum_bonds(np.rot90(grid, k=1, axes=(0, 2))),
        ]
    )
    return s


# test_find_bonds()


def test_place_droplets_count_bonds():
    g = make_empty_numpy_grid(2, 4, 6)
    # print(g, "\n\n\n")
    place_droplets(
        g,
        [
            "1,3,3",  # front
            "2,3,3",
            "2,2,3",
            "2,4,3",
            "2,3,2",
            "2,3,4",
            "3,3,3",  # back
        ],
    )
    # print(g)
    iter_sum_bonds_all_projections(g)
    # should be 2,2,2


test_place_droplets_count_bonds()


# test

x_max, y_max, z_max = get_grid_dimensions(test)

print("max of z, y, x:", z_max, y_max, x_max)

degrees_of = len(test) * 6

grid = make_empty_numpy_grid(z_max, x_max, y_max)

filled_grid = place_droplets(grid, test)

bonds = iter_sum_bonds_all_projections(filled_grid)

print(f" vacancies: {degrees_of}, bonds: {bonds}, surface_area: {degrees_of - bonds}")

# real

x_max, y_max, z_max = get_grid_dimensions(aoc_18)

print("max of z, y, x:", z_max, y_max, x_max)

degrees_of = len(aoc_18) * 6

grid = make_empty_numpy_grid(z_max, x_max, y_max)

filled_grid = place_droplets(grid, aoc_18)

bonds = iter_sum_bonds_all_projections(filled_grid)

print(f" vacancies: {degrees_of}, bonds: {bonds}, surface_area: {degrees_of - bonds}")

## works, but inefficient :D
## part 2 is not working with this method
