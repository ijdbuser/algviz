from string import ascii_uppercase

from ADT.BinaryMinHeap import BinaryMinHeap
from ADT.Graph import Graph
from ADT.Graph import Node, Edge


class DikstaNode(Node):
    label: str

    def __init__(self, label, d):
        super().__init__(label)
        self.d = d

    def __eq__(self, other):
        return self.label == other.label

    def __ne__(self, other):
        return self.label != other.label

    def __lt__(self, other):
        return self.d < other.d

    def __gt__(self, other):
        return self.d > other.d

    def __le__(self, other):
        return self.d <= other.d

    def __ge__(self, other):
        return self.d >= other.d

    def __str__(self):
        return f"{self.label}: {self.d}"

    def __repr__(self):
        return self.__str__()

class DikstaEdge(Edge):
    start: DikstaNode
    end: DikstaNode
    def __init__(self, start: DikstaNode, end: DikstaNode, w: int):
        super().__init__(start, end, w)

    def __str__(self):
        return f"({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

class DikstaGraph(Graph):
    E: list[DikstaEdge]
    V: list[DikstaNode]

    def __init__(self, E: list[DikstaEdge], V: list[DikstaNode]):
        super().__init__(E, V)

    def e_by_v(self, v) -> list[DikstaEdge]:
        res = []
        for edge in self.E:
            if edge.start == v:
                res.append(edge)

        return res


def diskta(graph: DikstaGraph, s: int):

    queue = BinaryMinHeap[DikstaNode]()

    for node in graph.V:
        queue.insert(node)
    x = []
    while len(queue) > 0:
        v = queue.extract_min()
        print(v, graph.e_by_v(v))
        for edge in graph.e_by_v(v):
            if edge.end.d > v.d + edge.w:
                edge.end.d = v.d + edge.w
                x.append(edge)
                queue.reorg(edge.end)

    edges = sorted(x, key=lambda k: k.end.d)

    return edges


if __name__ == "__main__":
    A, B, C, D, E, F, G = [DikstaNode(label=ascii_uppercase[i],
                                      d=float('inf')) for i in range(0, 7)]

    V = [A, B, C, D, E, F, G]
    pairs = [(A, B), (A, C), (A, D), (D, B), (B, C), (C, E), (E, F), (G, E), (G, F), (F, D)]
    vals = [1, 3, 2, 3, 4, 4, 2, 5, 3, 4]
    E = []
    for i, pair in enumerate(pairs):
        E.append(DikstaEdge(pair[0], pair[1], vals[i]))

    graph = DikstaGraph(E, V)
    V[0].d = 0

    import networkx as nx
    # importing matplotlib.pyplot
    import matplotlib.pyplot as plt

    g = nx.DiGraph()
    path = diskta(graph, 0)
    for el in graph.E:
        g.add_edge(el.start.label, el.end.label, color='grey', weight=el.w)

    for el in path:
        g.add_edge(el.start.label, el.end.label, color='red', weight=el.w)

    colors = nx.get_edge_attributes(g, 'color').values()
    weights = nx.get_edge_attributes(g, 'weight').values()
    w = nx.get_edge_attributes(g, 'weight').values()
    labels = nx.get_edge_attributes(g, 'weight')

    pos = nx.kamada_kawai_layout(g, scale=1.5)
    nx.draw(g, pos,
            edge_color=colors,
            width=list(weights),
            with_labels=True,
            node_color='lightgreen',
            arrows=True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()
