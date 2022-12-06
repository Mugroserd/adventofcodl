with open("input") as f:
    for line in f:
        for i in range(1, len(line) - 4):
            if line[i: i + 4].count(line[i]) == 1 and line[i: i + 4].count(line[i + 1]) == 1 \
                    and line[i: i + 4].count(line[i + 2]) == 1 and line[i: i + 4].count(line[i + 3]) == 1:
                print(i+4)
                break
