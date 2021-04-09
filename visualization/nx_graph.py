import networkx as nx
import matplotlib.pyplot as plt


def display_weighted_nx_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def display_nx_graph(graph: nx.Graph):
    nx.draw(graph, with_labels=True)
    plt.draw()
    plt.show()


def display_nx_digraph(graph: nx.DiGraph):
    pos = nx.shell_layout(graph)
    nx.draw(graph, pos, node_size=1000, with_labels=True, connectionstyle='arc3, rad = 0.25')
    plt.draw()
    plt.show()


def display_weighted_nx_di_graph(graph):
    pos = nx.shell_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.15)
    plt.show()