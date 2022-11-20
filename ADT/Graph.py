from __future__ import annotations

class Node:
    label = None

    def __init__(self, label):
        self.label = label


class Edge:
    start: Node
    end: Node
    w: int

    def __init__(self, start: Node, end: Node, w: int):
        self.start = start
        self.end = end
        self.w = w

    def __eq__(self, other: Edge):
        if (other.end == self.end and other.start == self.start) or (other.end == self.start and other.start == self.end):
            return True
        else:
            return False


class Graph:
    E: list[Edge]
    V: list[Node]

    def __init__(self, E: list[Edge], V: list[Node]):
        self.E = E
        self.V = V

    def __len__(self):
        return len(self.V)

    def get_edges_from_v(self, v: Node):
        res = []
        for edge in self.E:
            if edge.start == v:
                res.append(edge)
        return res