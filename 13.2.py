import ast
import random


class Packet:
    def __init__(self, packet):
        self.signal = packet

    def compare(self, right_packet) -> bool:
        list_left = self.signal
        list_right = right_packet.signal
        return compare(list_left, list_right)

    def __str__(self):
        return str(self.signal)


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
                return compare([list_left[i]], list_right[i])
            if not isinstance(list_right[i], list):
                return compare(list_left[i], [list_right[i]])
        elif isinstance(list_left[i], list) and isinstance(list_right[i], list):
            return compare(list_left[i], list_right[i])
        elif i == len(list_left) and i < len(list_right):
            return True
    return True # huli


def sort_packets(packets):
    n = len(packets)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not packets[j].compare(packets[j + 1]):
                swapped = True
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

        if not swapped:
            return


if __name__ == "__main__":
    packets = []
    index = 0
    indeces = 0
    with open("input") as f:
        for first in f:
            second = f.readline()
            packets.append(Packet(ast.literal_eval(first[:-1])))
            packets.append(Packet(ast.literal_eval(second[:-1])))
            index += 2
            f.readline()
    random.shuffle(packets)
    sort_packets(packets)
    start = 0
    end = 0
    for i, packet in enumerate(packets):
        if packet.signal == [[2]]:
            start = i + 1
        if packet.signal == [[6]]:
            end = i + 1
        print(packet)
    print(start * end)
