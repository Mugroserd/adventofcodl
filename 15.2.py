class WorldMap:
    class Beacon:
        def __init__(self, y, x):
            self.y = y
            self.x = x

    class Sensor:
        def __init__(self, y, x, beacon_y, beacon_x):
            self.y = y
            self.x = x
            self.beacon_y = beacon_y
            self.beacon_x = beacon_x
            self.coverage_left, self.coverage_right, self.coverage_up, self.coverage_down = 0, 0, 0, 0
            self.calculate_coverage()

        def calculate_coverage(self):
            y_diff = self.y - self.beacon_y
            x_diff = self.x - self.beacon_x
            distance = abs(x_diff) + abs(y_diff)
            self.coverage_left, self.coverage_right, self.coverage_up, self.coverage_down = \
                self.x - distance, self.x + distance, self.y - distance, self.y + distance

        def is_position_in_coverage(self, y, x) -> bool:
            y_diff = self.y - y
            x_diff = self.x - x
            distance = abs(x_diff) + abs(y_diff)
            return self.x - self.coverage_left >= distance

    def __init__(self):
        self.sensors = []
        self.beacons = set()

    def add_sensor(self, sensor_y, sensor_x, beacon_y, beacon_x):
        self.sensors.append(self.Sensor(sensor_y, sensor_x, beacon_y, beacon_x))

    def add_beacon(self, beacon_y, beacon_x):
        self.beacons.add(self.Beacon(beacon_y, beacon_x))

    def check_cell_on(self, y, x):
        reachable = False
        for sensor in self.sensors:
            reachable = reachable or sensor.is_position_in_coverage(y, x)
            if reachable:
                break
        return reachable


if __name__ == "__main__":
    TOP = 4000000
    world_map = WorldMap()
    with open("input") as f:
        for line in f:
            line = line[:-1]
            first, second = [a for a in line.split(': closest beacon is at x=')]
            sensor_x, sensor_y = [int(a) for a in first[12:].split(', y=')]
            beacon_x, beacon_y = [int(a) for a in second.split(', y=')]
            world_map.add_beacon(beacon_y, beacon_x)
            world_map.add_sensor(sensor_y, sensor_x, beacon_y, beacon_x)

    result_y = 0
    result_x = 0
    for i, sensor in enumerate(world_map.sensors):
        print(f"Sensor number {i}")
        y = sensor.coverage_down
        x = sensor.x
        checked = True
        while checked:
            if 0 <= x < TOP and 0 <= y <= TOP:
                checked = world_map.check_cell_on(y, x + 1)
                if not checked:
                    result_y = y
                    result_x = x + 1
            elif TOP < x or 0 > y or x > sensor.coverage_right or y < sensor.y:
                break
            x += 1
            y -= 1
        if not checked:
            break

    print(result_x, result_y)
    print(result_x * TOP + result_y)
