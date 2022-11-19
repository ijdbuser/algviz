from string import ascii_uppercase

from ADT.DisjointSetADT import DisjointSet, DisjointSetGraph, DisjointSetGraphEdge, DisjointSetGraphNode


def kruskal_mst(graph: DisjointSetGraph):
    T: list[DisjointSetGraphEdge]= []

    sorted_edges = sorted(graph.E, key=lambda k: k.w)

    for e in sorted_edges:
        v1, v2 = e.end, e.start

        if DisjointSet.find_set(v1) != DisjointSet.find_set(v2):
            DisjointSet.union(v1, v2)
            T.append(e)

    return T


if __name__ == "__main__":
    A, B, C, D, E, F, G = [DisjointSetGraphNode(i, ascii_uppercase[i]) for i in range(0, 7)]

    V = [A, B, C, D, E, F, G]
    pairs = [(A, B), (A, C), (A, D), (D, B), (B, C), (C, E), (E, F), (G, E), (G, F), (F, D)]
    vals = [1, 3, 2, 3, 4, 4, 2, 5, 3, 4]
    E = []
    for i, pair in enumerate(pairs):
        E.append(DisjointSetGraphEdge(pair[0], pair[1], vals[i]))

    graph = DisjointSetGraph(E, V)
    import networkx as nx
    # importing matplotlib.pyplot
    import matplotlib.pyplot as plt

    g = nx.Graph()

    for el in graph.E:
        g.add_edge(el.end, el.start, color='grey', w=el.w)

    for el in kruskal_mst(graph):
        g.add_edge(el.end, el.start, color='r', w=el.w)

    colors = nx.get_edge_attributes(g, 'color').values()
    weights = nx.get_edge_attributes(g, 'weight').values()
    w = nx.get_edge_attributes(g, 'w').values()
    labels = nx.get_edge_attributes(g, 'w')

    pos = nx.spectral_layout(g)
    nx.draw(g, pos,
            edge_color=colors,
            width=list(weights),
            with_labels=True,
            node_color='lightgreen')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()