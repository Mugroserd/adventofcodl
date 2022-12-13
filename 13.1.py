import ast


def compare(list_left, list_right) -> bool:

    for i in range(len(list_left)):
        if i == len(list_right):
            return False
        if not isinstance(list_left[i], list) and not isinstance(list_right[i], list):
            if list_left[i] > list_right[i]:
                return False
            elif list_left[i] < list_right[i]:
                return True
        elif not isinstance(list_left[i], list) or not isinstance(list_right[i], list):
            if not isinstance(list_left[i], list):
                list_left[i] = [list_left[i]]
            if not isinstance(list_right[i], list):
                list_right[i] = [list_right[i]]
            return compare(list_left[i], list_right[i])
        elif isinstance(list_left[i], list) and isinstance(list_right[i], list):
            return compare(list_left[i], list_right[i])
        elif i == len(list_left) and i < len(list_right):
            return True
    return True # huli


if __name__ == "__main__":
    pairs = []
    index = 1
    indeces = 0
    with open("input") as f:
        for first in f:
            second = f.readline()
            pairs.append([ast.literal_eval(first[:-1]), ast.literal_eval(second[:-1]), index])
            index += 1
            f.readline()
    for pair in pairs:
        if not isinstance(pair[0], list):
            pair[0] = [pair[0]]
        if not isinstance(pair[1], list):
            pair[1] = [pair[1]]
        if compare(pair[0], pair[1]):
            indeces += (pair[2])
    print(indeces)
