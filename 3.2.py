def calculate_weight(item: str) -> int:
    if item.islower():
        return (ord(item) - 96)
    else:
        return ord(item) - 38

score = 0
with open("input") as f:
    while True:
        line1 = f.readline()[:-1]
        line2 = f.readline()[:-1]
        line3 = f.readline()[:-1]
        if not line3: break
        for item in line1:
            if item in line2 and item in line3 :
                print(f"Item: {item}, calculated_weight: {calculate_weight(item)}")
                score += calculate_weight(item)
                break
print(score)