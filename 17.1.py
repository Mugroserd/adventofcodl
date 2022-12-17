from itertools import cycle


class Shape:
    class GenericShape:
        def __init__(self):
            self.landed = False
            self.cells = None

        def try_to_move(self, movement, cells_map):
            move_shape = True
            for i, cell in enumerate(self.cells):
                y, x = cell
                if not 0 <= x + movement < 7:
                    move_shape = False
                    break
                elif (y, x + movement) in cells_map:
                    move_shape = False
                    break
                else:
                    pass
            if move_shape:
                self.cells = [tuple(map(sum, zip(a, (0, movement)))) for a in self.cells]

        def lower(self, cells_map):
            lower_shape = True
            for i, cell in enumerate(self.cells):
                y, x = cell
                if 0 == y:
                    lower_shape = False
                    self.landed = True
                    break
                elif (y - 1, x) in cells_map:
                    lower_shape = False
                    self.landed = True
                    break
                else:
                    pass
            if lower_shape:
                self.cells = [tuple(map(sum, zip(a, (-1, 0)))) for a in self.cells]

    class HorLine(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells = [(y_bot, 2), (y_bot, 3), (y_bot, 4), (y_bot, 5)]

    class Cross(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells =          [(y_bot + 2, 3),
                   (y_bot + 1, 2), (y_bot + 1, 3), (y_bot + 1, 4), # так надо
                                   (y_bot,     3)]

    class Angle(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells =          [(y_bot + 2, 4),
                                   (y_bot + 1, 4),
           (y_bot, 2), (y_bot, 3), (y_bot,     4)]

    class VerLine(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells = [(y_bot,     2),
                          (y_bot + 1, 2),
                          (y_bot + 2, 2),
                          (y_bot + 3, 2)]

    class Box(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells = [(y_bot + 1, 2), (y_bot + 1, 3),
                          (y_bot,     2), (y_bot,     3)]

    class CleanerLine(GenericShape):
        def __init__(self, y_bot):
            super().__init__()
            self.cells = [(y_bot, 0), (y_bot, 1), (y_bot, 2), (y_bot, 3), (y_bot, 4), (y_bot, 5), (y_bot, 6)]

        def can_lower_until_split(self, cells_map):
            reached_end = 0
            while reached_end != 7:
                reached_end = 0
                for i, cell in enumerate(self.cells):
                    if (cell[0] - 1, cell[1]) in cells_map:
                        reached_end += 1
                    else:
                        self.cells[i] = (cell[0] - 1, cell[1])
            for i in range(1, 7):
                if abs(self.cells[i - 1][0] - self.cells[i][0]) > 2:
                    return False
            return True

    cur_shape = cycle(([
        HorLine,
        Cross,
        Angle,
        VerLine,
        Box]
    ))

    @staticmethod
    def new_shape(highest_rock):
        return next(Shape.cur_shape)(highest_rock)


class Movement:
    def __init__(self, direction):
        self.direction = 1 if direction == '>' else -1


def readjust_cells(cells_map, generator_layer):
    cleaner = Shape.CleanerLine(generator_layer)
    if not cleaner.can_lower_until_split(cells_map):
        return cells_map
    else:
        boundary = min([y for y, x in cleaner.cells]) - 1
        filter_arr = []
        for i in range(len(cells_map)):
            if cells_map[i][0] >= boundary:
                filter_arr.append(cells_map[i])
        return filter_arr


max_rocks = 2022
cells_map = [(-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6)]
if __name__ == "__main__":
    with open("input") as f:
        movements = cycle([Movement(a) for a in list(map(str, f.readline()[:-1]))])

    generator_layer = 3
    for rocks in range(max_rocks):
        shape = Shape.new_shape(generator_layer)
        while not shape.landed:
            shape.try_to_move(next(movements).direction, cells_map)
            shape.lower(cells_map)
        cells_map.extend(shape.cells)
        generator_layer = max([y for y, x in cells_map]) + 4
        # cells_map = readjust_cells(cells_map, generator_layer)
    print(generator_layer - 3)
