class Processor:

    def __init__(self):
        self.register = 1
        self.checked_days = {}
        self.ticks = 1

    def tick(self):
        if self.ticks % 20 == 0:
            self.checked_days[self.ticks] = self.register
        self.ticks += 1

    def check_input(self, line: list):
        self.tick()
        if len(line) > 1:
            self.register += int(line[1])
            self.tick()


cpu = Processor()
if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line[:-1].split(' ')
            cpu.check_input(line)
    print(cpu.checked_days)

result = 0
for day in cpu.checked_days.keys():
    if not day % 40 == 0:
        print(f"{day} {cpu.checked_days[day]} {day * cpu.checked_days[day]}")
        result += day * cpu.checked_days[day]
print(result)
