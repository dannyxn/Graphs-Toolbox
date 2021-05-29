import networkx as nx


def kosaraju(G: nx.DiGraph) -> list:
    g = nx.to_dict_of_lists(G)

    d = [-1 for _ in g]
    f = [-1 for _ in g]
    t = 0

    for v in G:
        if d[v] == -1:
            t = DFS_visit(v, g, d, f, t)

    Gt = G.reverse(True)
    gt = nx.to_dict_of_lists(Gt)
    nr = 0
    comp = [-1 for _ in g]

    for v in sorted(gt, key=lambda x: f[x], reverse=True):
        if comp[v] == -1:
            nr = nr + 1
            comp[v] = nr
            Components_R(nr, v, gt, comp)

    return comp


def DFS_visit(v: int, g: dict, d: list, f: list, t: int) -> int:
    t = t + 1
    d[v] = t

    for u in g[v]:
        if d[u] == -1:
            t = DFS_visit(u, g, d, f, t)

    t = t + 1
    f[v] = t
    return t


def Components_R(nr: int, v: int, g: dict, comp: list):
    for u in g[v]:
        if comp[u] == -1:
            comp[u] = nr
            Components_R(nr, u, g, comp)


def component_list(G) -> dict:
    comp = kosaraju(G)
    adjency_list = {}
    check = False
    k = 1
    while not check:
        check = True
        for i in range(0, len(comp)):
            if comp[i] == k:
                if check:
                    adjency_list[k] = []
                adjency_list[k].append(i)
                check = False
        k = k + 1

    return adjency_list
