from heapq import *
from collections import defaultdict


class Node:
    is_visited = False

    def __init__(self, node, height_pos, len_pos):
        self.height = node
        self.height_pos = height_pos
        self.len_pos = len_pos


class Graph:
    def __init__(self, full_map):
        self.nodes = []
        self.start_x_pos = 0
        self.start_y_pos = 0
        self.target_x_pos = 0
        self.target_y_pos = 0
        for height_pos, nodes in enumerate(full_map):
            self.nodes.append([])
            for len_pos, node in enumerate(nodes):
                if node == -1:
                    self.start_x_pos, self.start_y_pos = len_pos, height_pos
                    self.nodes[height_pos].append(Node(0, height_pos, len_pos))
                elif node == 99:
                    self.target_x_pos, self.target_y_pos = len_pos, height_pos
                    self.nodes[height_pos].append(Node(get_weight('z') + 1, height_pos, len_pos))
                else:
                    self.nodes[height_pos].append(Node(node, height_pos, len_pos))
            self.length = len(nodes)
        self.height = len(full_map)
        self.graph = []
        self.init_graph()

    def init_graph(self):
        graph = []
        for line in self.nodes:
            for node in line:
                try:
                    graph.append([node, self.nodes[node.height_pos + 1][node.len_pos]])
                except IndexError:
                    pass
                if abs(graph[-1][0].len_pos - graph[-1][1].len_pos) > 3 or \
                        abs(graph[-1][0].height_pos - graph[-1][1].height_pos) > 3 or \
                        graph[-1][1].height - graph[-1][0].height > 1:
                    graph = graph[:-1]
                try:
                    graph.append([node, self.nodes[node.height_pos][node.len_pos + 1]])
                except IndexError:
                    pass
                if abs(graph[-1][0].len_pos - graph[-1][1].len_pos) > 3 or \
                        abs(graph[-1][0].height_pos - graph[-1][1].height_pos) > 3 or \
                        graph[-1][1].height - graph[-1][0].height > 1:
                    graph = graph[:-1]
                try:
                    graph.append([node, self.nodes[node.height_pos - 1][node.len_pos]])
                except IndexError:
                    pass
                if abs(graph[-1][0].len_pos - graph[-1][1].len_pos) > 3 or \
                        abs(graph[-1][0].height_pos - graph[-1][1].height_pos) > 3 or \
                        graph[-1][1].height - graph[-1][0].height > 1:
                    graph = graph[:-1]
                try:
                    graph.append([node, self.nodes[node.height_pos][node.len_pos - 1]])
                except IndexError:
                    pass
                if abs(graph[-1][0].len_pos - graph[-1][1].len_pos) > 3 or \
                        abs(graph[-1][0].height_pos - graph[-1][1].height_pos) > 3 or \
                        graph[-1][1].height - graph[-1][0].height > 1:
                    graph = graph[:-1]
        self.graph = graph

    def calculate_shortest_path(self):
        shortest_path, nodes_amt = 0, 0
        paths = []
        return shortest_path, nodes_amt


def get_weight(symbol: str) -> int:
    return ord(symbol) - ord('a')


if __name__ == "__main__":
    full_map = []
    with open("input") as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines):
            full_map.append([])
            line = line[:-1]
            for symbol_number, symbol in enumerate(line):
                if symbol == 'S':
                    full_map[line_number].append(-1)
                elif symbol == 'E':
                    full_map[line_number].append(99)
                else:
                    full_map[line_number].append(get_weight(symbol) + 1)
        graph = Graph(full_map)
        path_length, path_nodes = graph.calculate_shortest_path()
        # for neighbors in graph.graph:
        #     print(neighbors[0].height, neighbors[1].height)
        #     print(neighbors[0].height_pos, neighbors[1].height_pos)
        #     print(neighbors[0].len_pos, neighbors[1].len_pos)
        #     print()
    print(graph.start_x_pos, graph.start_y_pos, graph.target_x_pos, graph.target_y_pos)
