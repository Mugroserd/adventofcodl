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

    def count_visible_trees(self):
        count = 0
        for row_num, row in enumerate(self.rows):
            for column_num, tree in enumerate(row):
                if not self.seek_higher_neighbors(tree, row_num, column_num):
                    count += 1
        return count

    def seek_higher_neighbors(self, tree, row, column, direction=None):
        if column == 0 or column == self.map_length or row == 0 or row == self.map_height:
            return False
        elif direction is None:
            left = self.seek_higher_neighbors(tree, row, column, direction="LEFT")
            right = self.seek_higher_neighbors(tree, row, column, direction="RIGHT")
            up = self.seek_higher_neighbors(tree, row, column, direction="UP")
            down = self.seek_higher_neighbors(tree, row, column, direction="DOWN")
            return left and right and up and down
        elif direction == "LEFT":
            if tree.height > self.rows[row][column - 1].height:
                return self.seek_higher_neighbors(tree, row, column - 1, direction=direction)
            else:
                return True
        elif direction == "RIGHT":
            if tree.height > self.rows[row][column + 1].height:
                return self.seek_higher_neighbors(tree, row, column + 1, direction=direction)
            else:
                return True
        elif direction == "UP":
            if tree.height > self.rows[row - 1][column].height:
                return self.seek_higher_neighbors(tree, row - 1, column, direction=direction)
            else:
                return True
        elif direction == "DOWN":
            if tree.height > self.rows[row + 1][column].height:
                return self.seek_higher_neighbors(tree, row + 1, column, direction=direction)
            else:
                return True

    def finalize(self):
        self.map_length = len(self.rows[0]) - 1
        self.map_height = len(self.rows) - 1


class Tree:
    def __init__(self, height):
        self.height = int(height)

    def __str__(self):
        return str(self.height)


if __name__ == "__main__":
    trees = TreeMap()
    with open("input") as f:
        for row_num, line in enumerate(f):
            line = line[:-1]
            trees.add_new_row()
            for column_num, height in enumerate(line):
                trees.add_tree(row_num, height)
    trees.finalize()
    print(trees.count_visible_trees())
