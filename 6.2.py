with open("input") as f:
    for line in f:
        for i in range(1, len(line) - 14):
            count = 0
            for symbol in line[i: i + 14]:
                if line[i: i + 14].count(symbol) == 1:
                    count += 1
                    if count == 14:
                        print(i+14)
                        break
                else:
                    break
