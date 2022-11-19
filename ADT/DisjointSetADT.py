from __future__ import annotations

from ADT.Graph import Node, Graph, Edge


# The Disjoint Set ADT


class DisjointSet:
    val: Node
    rank: int
    parent: DisjointSet

    def __init__(self, v: Node, parent=None):
        self.val = v
        if parent is None:
            self.rank = 0
            self.parent = self
        else:
            self.rank = parent.rank
            self.parent = parent

    @staticmethod
    def find_set(x: DisjointSet):
        """
        Finds the representative of the set
        """
        if x.parent != x:
            return DisjointSet.find_set(x.parent)
        return x

    @staticmethod
    def link(x: DisjointSet, y: DisjointSet):
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    @staticmethod
    def union(x: DisjointSet, y: DisjointSet):
        return DisjointSet.link(DisjointSet.find_set(x), DisjointSet.find_set(y))


class DisjointSetGraphNode(Node, DisjointSet):
    def __init__(self, x, name: str):
        Node.__init__(self, x)
        DisjointSet.__init__(self, self)
        self.name = name

    def __str__(self):
        return self.name


class DisjointSetGraphEdge(Edge):
    def __init__(self, start: DisjointSetGraphNode, end: DisjointSetGraphNode, w: int):
        super().__init__(start, end, w)

    def __str__(self):
        return f"({self.end}, {self.start})"


class DisjointSetGraph(Graph):
    def __init__(self, E: list[DisjointSetGraphEdge], V: list[DisjointSetGraphNode]):
        super().__init__(E, V)

