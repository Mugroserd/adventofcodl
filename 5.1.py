if __name__ == '__main__':
    result = {1: [],
              2: [],
              3: [],
              4: [],
              5: [],
              6: [],
              7: [],
              8: [],
              9: []
              }

    with open("input") as f:
        for line in f:
            if line[0] == '[':
                line = line.replace('[', '')
                line = line.replace('    ', ']')
                line = line.replace(']', ',')
                line = line.replace(' ', '')
                boxes = line.split(',')
                for i in range(0, len(boxes)-1):
                    if not boxes[i] == '':
                        result[i+1].append(boxes[i])
            elif line[0] == ' ':
                continue
            elif line[0] == 'm':
                line = line.replace('move ', '')
                line = line.replace(' from ', ',')
                line = line.replace(' to ', ',')
                move, from_num, to_num = [int(a) for a in line.split(',')]
                moving_boxes = result[from_num][:move]
                del result[from_num][:move]
                moving_boxes.reverse()
                result[to_num] = moving_boxes + result[to_num]
    for a in result.values():
        print(a[0], end='')
