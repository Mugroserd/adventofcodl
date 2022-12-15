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

        def is_row_in_coverage(self, row) -> bool:
            return self.coverage_up < row < self.coverage_down

        def get_left_pos_on_row(self, row):
            return self.coverage_left + abs(self.y - row)

        def get_right_pos_on_row(self, row):
            return self.coverage_right - abs(self.y - row)

    def __init__(self):
        self.sensors = []
        self.beacons = set()
        self.min_x = 10000000
        self.max_x = -10000000

    def add_sensor(self, sensor_y, sensor_x, beacon_y, beacon_x):
        self.sensors.append(self.Sensor(sensor_y, sensor_x, beacon_y, beacon_x))

    def add_beacon(self, beacon_y, beacon_x):
        self.beacons.add(self.Beacon(beacon_y, beacon_x))

    def check_sensors(self, row: int):
        for sensor in self.sensors:
            if sensor.is_row_in_coverage(row):
                self.min_x = min(self.min_x, sensor.get_left_pos_on_row(row))
                self.max_x = max(self.max_x, sensor.get_right_pos_on_row(row))


if __name__ == "__main__":
    world_map = WorldMap()
    with open("input") as f:
        for line in f:
            line = line[:-1]
            first, second = [a for a in line.split(': closest beacon is at x=')]
            sensor_x, sensor_y = [int(a) for a in first[12:].split(', y=')]
            beacon_x, beacon_y = [int(a) for a in second.split(', y=')]
            world_map.add_beacon(beacon_y, beacon_x)
            world_map.add_sensor(sensor_y, sensor_x, beacon_y, beacon_x)

    world_map.check_sensors(row=2000000)
    print(abs(world_map.max_x - world_map.min_x))
