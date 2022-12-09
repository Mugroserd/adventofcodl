class Direction:
    adjusts = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    def __init__(self, side: str):
        self.adjust = self.adjusts[side]


class Tail:
    pos = [0, 0]
    visited_cells = {(0, 0)}

    def update(self, next_point_x: int, next_point_y: int, next_point_last_pos: list[int], head_direction: Direction):
        if abs(self.pos[0] - next_point_x) > 1 or abs(self.pos[1] - next_point_y) > 1:
            if abs(self.pos[0] - next_point_x) + abs(self.pos[1] - next_point_y) > 2:
                self.pos = next_point_last_pos
            else:
                self.pos = [self.pos[0] + head_direction.adjust[0], self.pos[1] + head_direction.adjust[1]]
        self.visited_cells.add(tuple(self.pos))


class Head:
    pos = [0, 0]

    def step(self, direction: Direction, steps: int):
        for i in range(0, steps):
            last_pos = self.pos
            self.pos = [self.pos[0] + direction.adjust[0], self.pos[1] + direction.adjust[1]]
            tail.update(self.pos[0], self.pos[1], last_pos, direction)


head = Head()
tail = Tail()
if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line[:-1].split(' ')
            head.step(direction=Direction(line[0]), steps=int(line[1]))
    print(len(tail.visited_cells))
