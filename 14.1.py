class Cell:
    def __init__(self, type='VOID'):
        self.type = type
        self.is_falling = False
        if type == 'VOID':
            self.pixel = '.'
        elif type == 'STONE':
            self.pixel = '#'
        elif type == 'SAND':
            self.pixel = 'o'

    def __str__(self):
        return self.pixel


class WorldMap:
    def __init__(self, size):
        self.sand_y = None
        self.sand_x = None
        self.size = size
        self.grid = [[Cell()]]
        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append(Cell())

    def draw_stone_line(self, x_start, y_start, x_end, y_end):
        x_start, y_start, x_end, y_end = int(x_start), int(y_start), int(x_end), int(y_end)
        if abs(x_end - x_start) > abs(y_end - y_start):
            if x_start < x_end:
                for i in range(x_start, x_end + 1):
                    self.grid[y_start][i] = Cell(type='STONE')
            else:
                for i in range(x_end, x_start + 1):
                    self.grid[y_start][i] = Cell(type='STONE')
        else:
            if y_start < y_end:
                for j in range(y_start, y_end + 1):
                    self.grid[j][x_start] = Cell(type='STONE')
            else:
                for j in range(y_end, y_start + 1):
                    self.grid[j][x_start] = Cell(type='STONE')

    def get_cell(self, y, x) -> Cell:
        return self.grid[y][x]

    def add_sand(self, y, x):
        self.grid[y][x] = Cell(type='SAND')
        self.grid[y][x].is_falling = True
        self.sand_y = y
        self.sand_x = x

    def recalculate_sand_pos(self):
        if self.grid[self.sand_y + 1][self.sand_x].type == 'VOID':
            self.grid[self.sand_y + 1][self.sand_x], self.grid[self.sand_y][self.sand_x] = \
                self.grid[self.sand_y][self.sand_x], self.grid[self.sand_y + 1][self.sand_x]
            self.sand_y += 1
        elif self.grid[self.sand_y + 1][self.sand_x - 1].type == 'VOID':
            self.grid[self.sand_y + 1][self.sand_x - 1], self.grid[self.sand_y][self.sand_x] = \
                self.grid[self.sand_y][self.sand_x], self.grid[self.sand_y + 1][self.sand_x - 1]
            self.sand_y += 1
            self.sand_x += -1
        elif self.grid[self.sand_y + 1][self.sand_x + 1].type == 'VOID':
            self.grid[self.sand_y + 1][self.sand_x + 1], self.grid[self.sand_y][self.sand_x] = \
                self.grid[self.sand_y][self.sand_x], self.grid[self.sand_y + 1][self.sand_x + 1]
            self.sand_y += 1
            self.sand_x += 1
        else:
            self.grid[self.sand_y][self.sand_x].is_falling = False


if __name__ == "__main__":
    world_map = WorldMap(size=800)
    with open("input") as f:
        for line in f:
            stone_nodes = line[:-1].split(' -> ')
            stone_nodes = [a.split(',') for a in stone_nodes]
            for i in range(1, len(stone_nodes)):
                world_map.draw_stone_line(stone_nodes[i-1][0], stone_nodes[i-1][1],
                                          stone_nodes[i][0], stone_nodes[i][1])
    fallen_sands = 0
    out_of_boundary = False
    while not out_of_boundary:
        world_map.add_sand(0, 500)
        while world_map.get_cell(world_map.sand_y, world_map.sand_x).is_falling:
            world_map.recalculate_sand_pos()
            if world_map.sand_y > 700:
                out_of_boundary = True
                break

    fallen_sands = 0
    for i in range(0, world_map.size - 630):
        for j in range(0, world_map.size):
            if world_map.grid[i][j].type == 'SAND':
                fallen_sands += 1
            print(str(world_map.grid[i][j]), end='')
        print()

    print(fallen_sands)
