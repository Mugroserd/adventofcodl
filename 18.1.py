from itertools import cycle


class Cube:
    def __init__(self, x, y, z):
        self.connected = set()
        self.x, self.y, self.z = x, y, z

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


cubes = []
start = Cube(-1, -1, -1)
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
