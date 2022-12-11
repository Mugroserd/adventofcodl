monkeys = {}


class Golden:

    def __init__(self, item):
        self.name = str(item)
        self.dividers = {1}
        self.add_dividers(item)
        self.new_dividers = {1}

    def add_dividers(self, item):
        for i in range(1, item // 2 + 1):
            if item % i == 0:
                self.dividers.add(i)
        self.dividers.add(item)

    def add(self, number):
        result = self.get_number()
        for mu in self.new_dividers:
            result *= mu
        result += number
        self.dividers = {1}
        self.new_dividers = {1}

        self.add_dividers(result)

    def get_number(self):
        return max(self.dividers)


class Monkey:

    def __init__(self, current_monkey, items, operation_type, operation_subject, division_number, true_to_monkey, false_to_monkey):
        self.current_monkey = int(current_monkey)
        self.items = [Golden(int(a)) for a in items]
        self.operation_type = operation_type
        self.operation_subject = operation_subject
        self.division_number = int(division_number)
        self.true_to_monkey = int(true_to_monkey)
        self.false_to_monkey = int(false_to_monkey)
        self.throws = 0
        self.received_items = []

    def throw_item(self, item, monkey):
        monkeys[monkey].items.append(item)
        print(f"Monkey {self.current_monkey} thrown {item.name} weighing {item.get_number()} to Monkey {monkey}")
        self.throws += 1

    def check_throw(self):
        for item in self.items:
            if self.operation_type == '*':
                if self.operation_subject == 'old':
                    pass
                else:
                    item.dividers.add(int(self.operation_subject))
                    item.new_dividers.add(int(self.operation_subject))

                if self.division_number in item.dividers:
                    self.throw_item(item, self.true_to_monkey)
                else:
                    self.throw_item(item, self.false_to_monkey)

            elif self.operation_type == '+':
                if self.operation_subject == 'old':
                    item.dividers.add(2)
                    item.new_dividers.add(2)
                else:
                    item.add(int(self.operation_subject))

                if self.division_number in item.dividers:
                    self.throw_item(item, self.true_to_monkey)
                else:
                    self.throw_item(item, self.false_to_monkey)
        self.items = []

    def end_round(self):
        self.items = self.received_items.copy()
        self.received_items = []


def parse_monkey_actions(monkeys, monkey_num, starting_items, operation, test, true_operation, false_operation):
    current_monkey = monkey_num[-2]
    items = starting_items[18:].split(', ')
    operation_type = operation[23]
    operation_subject = operation[25:]
    division_number = test[21:]
    true_to_monkey = true_operation[29:]
    false_to_monkey = false_operation[30:]
    # print(monkey_num, starting_items, operation, test, true_operation, false_operation)
    # print(current_monkey, items, operation_type, operation_subject, division_number, true_to_monkey, false_to_monkey, sep='')
    monkeys[int(current_monkey)] = Monkey(current_monkey, items, operation_type, operation_subject,
                                          division_number, true_to_monkey, false_to_monkey)


if __name__ == "__main__":
    with open("input") as f:
        while True:
            parse_monkey_actions(monkeys, f.readline()[:-1], f.readline()[:-1], f.readline()[:-1],
                                 f.readline()[:-1], f.readline()[:-1], f.readline()[:-1])
            temp = f.readline()
            if not temp:
                break
    for i in range(4):
        for monkey in monkeys.values():
            monkey.check_throw()
        if i % 500 == 0:
            print("Monkey business in progress:" + str(i / 100))

for monkey in monkeys.values():
    print(monkey.throws)
