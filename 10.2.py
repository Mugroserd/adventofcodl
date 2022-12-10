class Processor:

    def __init__(self):
        self.register = 1
        self.lines = ['']
        self.ticks = 1

    def tick(self):
        if self.register <= self.ticks < self.register + 3:
            self.lines[-1] = self.lines[-1] + '#'
        else:
            self.lines[-1] = self.lines[-1] + '.'
        if self.ticks % 40 == 0:
            self.lines.append('')
            self.ticks = self.ticks - 40

        self.ticks += 1

    def check_input(self, line: list):
        self.tick()
        if len(line) > 1:
            self.tick()
            self.register += int(line[1])


cpu = Processor()
if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line[:-1].split(' ')
            cpu.check_input(line)

for line in cpu.lines:
    print(line)