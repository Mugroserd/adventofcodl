max_value = 0
max_value_2 = 0
max_value_3 = 0
inv_value = 0

with open("input") as f:
    for cur_line in f:
        if cur_line is not "\n":
            inv_value += int(cur_line)
            if inv_value > max_value:
                max_value = inv_value
            elif inv_value > max_value_2:
                max_value_2 = inv_value
            elif inv_value > max_value_3:
                max_value_3 = inv_value
        else:
            inv_value = 0
print(max_value + max_value_2 + max_value_3)