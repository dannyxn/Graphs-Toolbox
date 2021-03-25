from collections import defaultdict
from random import randint, random

from algorithms.coherent_component import GraphRepresentationType, GraphRepresentation, CoherentComponentFinder


def G_n_l(n, l) -> GraphRepresentation:
    G = defaultdict(list)
    [G.setdefault(x, []) for x in range(n)]
    for _ in range(l):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        while True:
            if y != x and y not in G[x]:
                break
            y = randint(0, n - 1)
        G[x].append(y)
        G[y].append(x)
    G = sorted(G.items())
    G = defaultdict(list, G)
    BG = defaultdict(list)
    [BG.setdefault(x, []) for x in range(n)]
    for i in G:
        l = []
        for j in G[i]:
            l.append(j)
        l.sort()
        for j in l:
            BG[i].append(j)
    graph = GraphRepresentation(GraphRepresentationType.ADJACENCY_LIST, BG)
    return graph


def generate_connected_graph(nodes, paths) -> GraphRepresentation:
    finder = CoherentComponentFinder()
    while True:
        graph = G_n_l(nodes, paths)
        graph.convert(GraphRepresentationType.ADJACENCY_MATRIX)
        if finder.check_if_graph_is_connected(graph):
            break
    return graph


# ta ponizej dalej zje*ana :)
def G_n_p(n, p):
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if random() < p:
                if i != j:
                    G[i].append(j + 1)
                    G[j].append(i + 1)
    return G
