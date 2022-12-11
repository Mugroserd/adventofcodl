monkeys = {}


class Monkey:

    def __init__(self, current_monkey, items, operation_type, operation_subject, division_number, true_to_monkey, false_to_monkey):
        self.current_monkey = int(current_monkey)
        self.items = [int(a) for a in items]
        self.operation_type = operation_type
        self.operation_subject = operation_subject
        self.division_number = int(division_number)
        self.true_to_monkey = int(true_to_monkey)
        self.false_to_monkey = int(false_to_monkey)
        self.throws = 0
        self.received_items = []

    def throw_item(self, item, monkey, unbothered_item):
        monkeys[monkey].items.append(item)
        # print(f"Monkey {self.current_monkey} thrown {item} to Monkey {monkey}")
        self.throws += 1

    def check_throw(self):
        for item in self.items:
            unbothered_item = item
            if self.operation_type == '*':
                if self.operation_subject == 'old':
                    item = item * item
                else:
                    item = item * int(self.operation_subject)
                if item % self.division_number == 0:
                    item = item % 9699690
                    self.throw_item(item, self.true_to_monkey, unbothered_item)
                else:
                    self.throw_item(item, self.false_to_monkey, unbothered_item)
            elif self.operation_type == '+':
                if self.operation_subject == 'old':
                    item = item * 2
                else:
                    item = item + int(self.operation_subject)
                if item % self.division_number == 0:
                    item = item % 9699690
                    self.throw_item(item, self.true_to_monkey, unbothered_item)
                else:
                    self.throw_item(item, self.false_to_monkey, unbothered_item)
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
    for i in range(10000):
        for monkey in monkeys.values():
            monkey.check_throw()

for monkey in monkeys.values():
    print(monkey.throws)
