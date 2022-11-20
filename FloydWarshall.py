from __future__ import annotations

from string import ascii_uppercase

from ADT.Graph import Graph, Node, Edge


class FloydWarshallNode(Node):
    index: int | None

    def __init__(self, label):
        super().__init__(label)
        self.index = None

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def __str__(self):
        return f"{self.label}"

    def __repr__(self):
        return self.__str__()


class FloydWarshallEdge(Edge):
    start: FloydWarshallNode
    end: FloydWarshallNode

    def __str__(self):
        return f"({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()


class FloydWarshallGraph(Graph):
    edges_table: list[list[FloydWarshallEdge | None]]
    V: list[FloydWarshallNode]
    E: list[FloydWarshallEdge]

    def __init__(self, E: list[FloydWarshallEdge], V: list[FloydWarshallNode]):
        super().__init__(E, V)
        self.edges_table = []
        n = len(V)
        for i in range(n):
            self.edges_table.append([None for _ in range(n)])

        for i, v in enumerate(self.V):
            v.set_index(i)

        for e in self.E:
            self.edges_table[e.start.get_index()][e.end.get_index()] = e

    def is_edge(self, start: FloydWarshallNode | int, end: FloydWarshallNode | int):
        if type(start) == int and type(end) == int:
            return self.edges_table[start][end]
        elif type(start) == FloydWarshallNode and type(end) == FloydWarshallNode:
            return self.edges_table[start.get_index()][end.get_index()]
        else:
            raise TypeError("Need both int or both node")


def floyd_warshall(graph: FloydWarshallGraph):
    n = len(graph)
    mem: list[list[float | None]] = []
    pathsL: list[list[list[FloydWarshallEdge]]] = []

    for x in range(0, n):
        mem.append([None for i in range(n)])
        for y in range(0, n):
            if x == y:
                mem[x][y] = 0
            elif graph.is_edge(x, y) is not None:
                mem[x][y] = graph.is_edge(x, y).w
            else:
                mem[x][y] = float("inf")

    for x in range(0, n):
        pathsL.append([[] for i in range(n)])
        for y in range(0, n):
            if mem[x][y] > 0 and mem[x][y] != float('inf'):
                pathsL[x][y].append(graph.is_edge(x, y))

    for k in range(0, n):# All vertices K
        for x in range(0, n): #All vertices X
            for y in range(0, n): #All vertices Y
                if mem[x][y] > mem[x][k] + mem[k][y]:
                    pathsL[x][y] = pathsL[x][k] + pathsL[k][y]

                mem[x][y] = min(mem[x][y],
                                mem[x][k] + mem[k][y])

    return mem, pathsL


if __name__ == "__main__":
    A, B, C, D, E, F, G = [
        FloydWarshallNode(label=ascii_uppercase[i]) for i in range(0, 7)
    ]

    V = [A, B, C, D, E, F, G]
    pairs = [
        (A, B),
        (A, C),
        (A, D),
        (D, B),
        (B, C),
        (C, E),
        (E, F),
        (G, E),
        (G, F),
        (F, D),
    ]
    vals = [1, 3, 2, 3, 4, 4, 2, 5, 3, 4]
    E = []
    for i, pair in enumerate(pairs):
        E.append(FloydWarshallEdge(pair[0], pair[1], vals[i]))

    graph = FloydWarshallGraph(E, V)

    import networkx as nx

    # importing matplotlib.pyplot
    import matplotlib.pyplot as plt

    mem, paths = floyd_warshall(graph)

    for x in range(len(graph)):
        print(f"{graph.V[x].label}:")
        for y in range(len(graph)):
            if x == y or mem[x][y] == float('inf') or mem[x][y] == 0:
                continue

            print(f"---- {graph.V[y]} {paths[x][y]} ({mem[x][y]})")

            g = nx.DiGraph()

            for el in graph.E:
                g.add_edge(el.start.label, el.end.label, color="grey", weight=el.w)

            path = paths[x][y]

            for el in path:
                g.add_edge(el.start.label, el.end.label, color="red", weight=el.w)

            colors = nx.get_edge_attributes(g, "color").values()
            weights = nx.get_edge_attributes(g, "weight").values()
            w = nx.get_edge_attributes(g, "weight").values()
            labels = nx.get_edge_attributes(g, "weight")

            pos = nx.kamada_kawai_layout(g, scale=1.5)
            nx.draw(
                g,
                pos,
                edge_color=colors,
                width=list(weights),
                with_labels=True,
                node_color="lightgreen",
                arrows=True,
            )
            nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
            plt.show()
