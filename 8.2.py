class TreeMap:
    rows = []
    map_length = 0
    map_height = 0

    def add_tree(self, row_num, height):
        self.rows[row_num].append(Tree(height))

    def __str__(self):
        output = ''
        for row in self.rows:
            output += ' '.join(str(tree) for tree in row)
            output += '\n'
        return output

    def add_new_row(self):
        self.rows.append([])

    def count_trees_prestige(self):
        for row_num, row in enumerate(self.rows):
            for column_num, tree in enumerate(row):
                self.seek_higher_neighbors(tree, row_num, column_num)
        for row in self.rows:
            for tree in row:
                tree.calculate_prestige()

    def seek_higher_neighbors(self, tree, row, column, direction=None):
        if column == 0 or column == self.map_length or row == 0 or row == self.map_height:
            if direction is None:
                tree.view_up = 0  # мне поебать какое
            elif direction == "LEFT":
                tree.view_left = tree.view_left - 1
            elif direction == "RIGHT":
                tree.view_right = tree.view_right - 1
            elif direction == "UP":
                tree.view_up = tree.view_up - 1
            elif direction == "DOWN":
                tree.view_down = tree.view_down - 1
        elif direction is None:
            self.seek_higher_neighbors(tree, row, column, direction="LEFT")
            self.seek_higher_neighbors(tree, row, column, direction="RIGHT")
            self.seek_higher_neighbors(tree, row, column, direction="UP")
            self.seek_higher_neighbors(tree, row, column, direction="DOWN")
        elif direction == "LEFT":
            if tree.height > self.rows[row][column - 1].height:
                tree.view_left += 1
                return self.seek_higher_neighbors(tree, row, column - 1, direction=direction)
            else:
                return True
        elif direction == "RIGHT":
            if tree.height > self.rows[row][column + 1].height:
                tree.view_right += 1
                return self.seek_higher_neighbors(tree, row, column + 1, direction=direction)
            else:
                return True
        elif direction == "UP":
            if tree.height > self.rows[row - 1][column].height:
                tree.view_up += 1
                return self.seek_higher_neighbors(tree, row - 1, column, direction=direction)
            else:
                return True
        elif direction == "DOWN":
            if tree.height > self.rows[row + 1][column].height:
                tree.view_down += 1
                return self.seek_higher_neighbors(tree, row + 1, column, direction=direction)
            else:
                return True

    def find_maximum_prestige(self):
        maximum_prestige = 0
        for row in self.rows:
            for tree in row:
                if maximum_prestige < tree.prestige:
                    maximum_prestige = tree.prestige
        return maximum_prestige

    def finalize(self):
        self.map_length = len(self.rows[0]) - 1
        self.map_height = len(self.rows) - 1


class Tree:
    view_left = 1
    view_right = 1
    view_up = 1
    view_down = 1
    prestige = 1

    def __init__(self, height):
        self.height = int(height)

    def __str__(self):
        return str(self.height) + " " + str(self.prestige)

    def calculate_prestige(self):
        self.prestige = self.view_left * self.view_right * self.view_up * self.view_down
        return self.prestige


if __name__ == "__main__":
    trees = TreeMap()
    with open("input") as f:
        for row_num, line in enumerate(f):
            line = line[:-1]
            trees.add_new_row()
            for column_num, height in enumerate(line):
                trees.add_tree(row_num, height)
    trees.finalize()
    print(trees.count_trees_prestige())
    print(trees.find_maximum_prestige())
