from pprint import pprint as p


aoc_8 = open("./AOC_door_8.txt", "r").read().splitlines()
aoc_8 = aoc_8  # [1:]


def func_fallback(lst, func=max, fallback=-1):
    if len(lst) == 0:
        return fallback  # as in non-existent
    else:
        return func(lst)


class Matrix(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[-1 for col in range(columns)] for row in range(rows)]

    def put_value(self, row, column, value):
        self.matrix[row][column] = int(value)

    def get_value(self, row, column):
        return self.matrix[row][column]

    def get_left(self, row, column):
        subset = self.matrix[row][:column]
        return subset

    def get_right(self, row, column):
        subset = self.matrix[row][column + 1 :]
        return subset

    def get_up(self, row, column):
        subset = [self.matrix[r][column] for r in range(0, row)]
        return subset

    def get_down(self, row, column):
        subset = [self.matrix[r][column] for r in range(row + 1, self.rows)]
        return subset

    def print_directions(self, row, column):
        print(
            "\nsubsets: L,R,U,D\n",
            self.get_left(row, column),
            self.get_right(row, column),
            self.get_up(row, column),
            self.get_down(row, column),
            "\n",
        )

    def is_visible(self, row, column):
        # the marginal ones
        if (
            row == 0
            or column == 0
            or row == self.rows - 1
            or column == self.columns - 1
        ):
            return True
        # the non-marginal ones
        own_height = self.get_value(row, column)
        visible_from_left = own_height > max(self.get_left(row, column))
        visible_from_right = own_height > max(self.get_right(row, column))
        visible_from_up = own_height > max(self.get_up(row, column))
        visible_from_down = own_height > max(self.get_down(row, column))
        is_visible = (
            visible_from_left
            or visible_from_right
            or visible_from_up
            or visible_from_down
        )
        return is_visible

    def visual_range_score(self, sight: list[int], threshold):
        if len(sight) == 0:  # margin cases
            return 1
        distance_scores = [
            ind + 1 for ind, height in enumerate(sight) if height >= threshold
        ]  # +1 because starting at 0
        if len(distance_scores) == 0:
            # if there is no obstracle, take the full range until margin
            return len(sight)
        else:
            farest_sight = func_fallback(
                distance_scores, func=min, fallback=1
            )  # taking the nearest
            return farest_sight

    def view_score(self, row, column):
        own_height = self.get_value(row, column)

        look_left = self.get_left(row, column)[::-1]
        look_right = self.get_right(row, column)
        look_up = self.get_up(row, column)[::-1]
        look_down = self.get_down(row, column)

        # print(look_left, look_right, look_up, look_down)

        score_left = self.visual_range_score(look_left, own_height)
        score_right = self.visual_range_score(look_right, own_height)
        score_up = self.visual_range_score(look_up, own_height)
        score_down = self.visual_range_score(look_down, own_height)

        # print(score_left, score_right, score_up, score_down)

        score = score_left * score_right * score_up * score_down
        return score

    @property
    def yield_matrix(self):
        return self.matrix

    @property
    def show(self):
        for row in self.matrix:
            print(row)


def test_0():
    trees = Matrix(10, 10)

    trees.put_value(5, 4, 8)
    trees.put_value(5, 6, 10)
    trees.put_value(5, 5, 8)
    trees.put_value(4, 5, 10)
    trees.put_value(6, 5, 10)

    trees.show

    p(trees.is_visible(5, 5))
    p(trees.is_visible(0, 3))
    p(trees.is_visible(1, 0))


def test_p1():
    test = """\
13213330
41040402
03421022
42144234
11400122
12442202
"""
    test = test.splitlines()
    rows = len(test)
    columns = len(test[0])
    forest = Matrix(rows, columns)

    for n_row, row in enumerate(test):
        for n_col, val in enumerate(row):
            forest.put_value(row=n_row, column=n_col, value=val)

    forest.show

    p("\n")

    # part 1 manual test
    # p(forest.get_left(row=1, column=1))  # works
    # p(forest.get_right(row=1, column=1))  # works
    # p(forest.get_up(row=1, column=1))  # works
    # p(forest.get_down(row=1, column=1))  # works
    # p(forest.is_visible(row=1, column=1))

    # return

    visible_trees = 0

    for n_row, row in enumerate(test):
        for n_col, val in enumerate(row):
            print("===")
            visible = forest.is_visible(row=n_row, column=n_col)
            print(f"n_row {n_row}, n_col {n_col}, value {val}, visible? {visible}")
            print("===")
            if visible:
                visible_trees += 1

    print(visible_trees)


# test_p1()


def test_p2():
    test = """\
13213330
41040402
03421022
42144234
11400122
12442202
"""
    test = test.splitlines()
    rows = len(test)
    columns = len(test[0])
    forest = Matrix(rows, columns)

    for n_row, row in enumerate(test):
        for n_col, val in enumerate(row):
            forest.put_value(row=n_row, column=n_col, value=val)

    forest.show

    p("\n")

    #### part 2 manual test
    # p(forest.view_score(2, 2))  # 40
    # p(forest.view_score(1, 1))  # 4
    # p(forest.view_score(0, 0))  # 1
    # p(forest.view_score(1, 4))  # 1
    # p(forest.view_score(3, 3))  # 8

    max_score = 0

    for n_row, row in enumerate(test):
        for n_col, val in enumerate(row):
            # print("===")
            score = forest.view_score(row=n_row, column=n_col)
            print(f"n_row {n_row}, n_col {n_col}, value {val}, score = {score}")
            # print("===")
            max_score = max(max_score, score)

    print(f"==> {max_score}")


# test_p2()


def part_1():
    rows = len(aoc_8)
    columns = len(aoc_8[0])
    n_margin = (2 * rows + 2 * columns) - 4

    forest = Matrix(rows, columns)

    for n_row, row in enumerate(aoc_8):
        for n_col, val in enumerate(row):
            forest.put_value(row=n_row, column=n_col, value=val)

    forest.show

    visible_trees = 0

    p(aoc_8)

    for n_row, row in enumerate(aoc_8):
        for n_col, val in enumerate(row):
            visible = forest.is_visible(row=n_row, column=n_col)
            print(f"n_row {n_row}, n_col {n_col}, value {val}, visible? {visible}")
            if visible:
                visible_trees += 1

    p(f"marinal trees: {n_margin}")
    p(f"visible_trees: {visible_trees}")


# part_1()


def part_2():
    rows = len(aoc_8)
    columns = len(aoc_8[0])
    n_margin = (2 * rows + 2 * columns) - 4

    forest = Matrix(rows, columns)

    for n_row, row in enumerate(aoc_8):
        for n_col, val in enumerate(row):
            forest.put_value(row=n_row, column=n_col, value=val)

    forest.show

    max_score = 0

    p(aoc_8)

    for n_row, row in enumerate(aoc_8):
        for n_col, val in enumerate(row):
            # print("===")
            score = forest.view_score(row=n_row, column=n_col)
            print(f"n_row {n_row}, n_col {n_col}, value {val}, score = {score}")
            # print("===")
            max_score = max(max_score, score)

    print(f"==> {max_score}")


part_2()
