def calculate_weight(item: str) -> int:
    if item.islower():
        return (ord(item) - 96)
    else:
        return ord(item) - 64 + 26

score = 0
with open("input") as f:
    for cur_line in f:
        cleaned_line = cur_line[:len(cur_line)-1]
        first_half = cleaned_line[:len(cleaned_line)//2]
        second_half = cleaned_line[len(cleaned_line)//2:]
        for item in first_half:
            if item in second_half:
                print(f"{first_half} {second_half}")
                print(f"Item: {item}, calculated_weight: {calculate_weight(item)}")
                score += calculate_weight(item)
                break
print(score)