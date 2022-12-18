from itertools import cycle


class Cube:
    def __init__(self, x, y, z):
        self.connected = set()
        self.x, self.y, self.z = x, y, z
        self.are_neighbours_checked = False
        self.connected_stones = 0

    def check_sides(self, brat):
        if abs(self.x - brat.x) == 1 and self.y == brat.y and self.z == brat.z:
            self.connected.add(brat)
            brat.connected.add(self)
        elif abs(self.y - brat.y) == 1 and self.x == brat.x and self.z == brat.z:
            self.connected.add(brat)
            brat.connected.add(self)
        elif abs(self.z - brat.z) == 1 and self.x == brat.x and self.y == brat.y:
            self.connected.add(brat)
            brat.connected.add(self)

    def append_air(self, temp):
        connected_cubes = set()
        for other in neigbours:
            if minni < self.x + other[0] < maxim          \
                    and minni < self.y + other[1] < maxim \
                    and minni < self.z + other[2] < maxim:
                x, y, z = self.x + other[0], self.y + other[1], self.z + other[2]
                if (x, y, z) in [(a.x, a.y, a.z) for a in cubes]:
                    self.connected_stones += 1
                elif (x, y, z) in [(a.x, a.y, a.z) for a in filler] or (x, y, z) in [(a.x, a.y, a.z) for a in temp]:
                    pass
                else:
                    connected_cubes.add(Cube(self.x + other[0], self.y + other[1], self.z + other[2]))
        self.are_neighbours_checked = True
        return connected_cubes


cubes = []
if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line[:-1]
            x, y, z = [int(a) for a in line.split(',')]
            cubes.append(Cube(x, y, z))
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            cubes[i].check_sides(cubes[j])

    print(sum([6 - len(a.connected) for a in cubes]))

    minni = -2
    maxim = 23
    neigbours = [(1, 0, 0), (-1, 0, 0),
                 (0, 1, 0), (0, -1, 0),
                 (0, 0, 1), (0, 0, -1)]

    start = Cube(-1, -1, -1)
    filler = set()
    filler.add(start)

    while True:
        temp = set()
        for cube in filler:
            if not cube.are_neighbours_checked:
                temp.update(cube.append_air(temp))
        filler.update(temp)

        flag = True
        for cube in filler:
            if not cube.are_neighbours_checked:
                flag = False
        if flag:
            break
    print(sum([a.connected_stones for a in filler]))
