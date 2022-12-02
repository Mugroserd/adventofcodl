games = {
"A X": 1+3, "A Y": 2+6, "A Z": 3+0,
"B X": 1+0, "B Y": 2+3, "B Z": 3+6,
"C X": 1+6, "C Y": 2+0, "C Z": 3+3,
}

total_score = 0
with open("input") as f:
    for cur_line in f:
        total_score += games[cur_line[0:3]]
print(total_score)