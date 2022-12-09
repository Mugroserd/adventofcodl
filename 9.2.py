from os import system
from time import sleep


class Direction:
    adjusts = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    def __init__(self, side: str):
        self.adjust = self.adjusts[side]


class Tail:
    def __init__(self, number):
        self.number = number
        self.visited_cells = {(0, 0)}
        self.last_pos = [0, 0]
        self.pos = [0, 0]

    def update(self, next_point_x: int, next_point_y: int, next_point_last_pos: list[int], head_direction: Direction):
        self.last_pos = [ohuel for ohuel in self.pos]
        if abs(self.pos[0] - next_point_x) > 1 or abs(self.pos[1] - next_point_y) > 1:
            if abs(self.pos[0] - next_point_x) + abs(self.pos[1] - next_point_y) > 2:
                # self.pos = next_point_last_pos
                self.pos = [self.pos[0] - int(abs(self.pos[0] - next_point_x) / (self.pos[0] - next_point_x)),
                            self.pos[1] - int(abs(self.pos[1] - next_point_y) / (self.pos[1] - next_point_y))]
            elif abs(self.pos[0] - next_point_x) == 2:
                self.pos[0] -= int(abs(self.pos[0] - next_point_x) / (self.pos[0] - next_point_x))
            elif abs(self.pos[1] - next_point_y) == 2:
                self.pos[1] -= int(abs(self.pos[1] - next_point_y) / (self.pos[1] - next_point_y))
        self.visited_cells.add(tuple(self.pos))


class Head:
    pos = [0, 0]

    def step(self, direction: Direction, steps: int):
        for i in range(0, steps):
            last_pos = self.pos
            self.pos = [self.pos[0] + direction.adjust[0], self.pos[1] + direction.adjust[1]]
            tails[0].update(self.pos[0], self.pos[1], last_pos, direction)
            for j in range(1, len(tails)):
                tails[j].update(tails[j - 1].pos[0], tails[j - 1].pos[1], tails[j - 1].last_pos, direction)

            # for y in range(30):
            #     line = ''
            #     for x in range(50):
            #         line += '[ ]'
            #         for tail in tails:
            #             if tail.pos[0] + 20 == x and tail.pos[1] + 20 == y:
            #                 line = line[:-3] + "[" + tail.number + "]"
            #     print(line)
            # sleep(1)
            # system('cls')
            # print(f"0 - {tails[0].last_pos} -> {tails[0].pos} reaching for {self.pos}")
            # print(f"1 - {tails[1].last_pos} -> {tails[1].pos} reaching for {tails[0].pos}")
            # print(f"2 - {tails[2].last_pos} -> {tails[2].pos} reaching for {tails[1].pos}")
            # print(f"3 - {tails[3].last_pos} -> {tails[3].pos} reaching for {tails[2].pos}")
            # print(f"4 - {tails[4].last_pos} -> {tails[4].pos} reaching for {tails[3].pos}")
            # print(f"5 - {tails[5].last_pos} -> {tails[5].pos} reaching for {tails[4].pos}")
            # print(f"6 - {tails[6].last_pos} -> {tails[6].pos} reaching for {tails[5].pos}")
            # print(f"7 - {tails[7].last_pos} -> {tails[7].pos} reaching for {tails[6].pos}")
            # print(f"8 - {tails[8].last_pos} -> {tails[8].pos} reaching for {tails[7].pos}")
            # print()


head = Head()
tails = [Tail("1"), Tail("2"), Tail("3"), Tail("4"), Tail("5"), Tail("6"), Tail("7"), Tail("8"), Tail("9")]
if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line[:-1].split(' ')
            head.step(direction=Direction(line[0]), steps=int(line[1]))
            print("Step finished")
    print(len(tails[8].visited_cells))

