import networkx as nx

import matplotlib.pyplot as plt


def display_weighted_nx_graph(G: nx.Graph):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def display_nx_graph(G: nx.Graph):
    nx.draw(G, with_labels=True)
    plt.draw()
    plt.show()


def display_nx_DiGraph(G: nx.DiGraph):
    pos = nx.shell_layout(G)
    nx.draw(G, pos, node_size=1000, with_labels=True, connectionstyle='arc3, rad = 0.25')
    plt.draw()
    plt.show()