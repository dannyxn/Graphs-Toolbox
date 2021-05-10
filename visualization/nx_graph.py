import matplotlib.pyplot as plt
import networkx as nx


def display_weighted_nx_graph(graph: nx.Graph, filename: str = ""):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    if filename:
        plt.savefig(filename)
    plt.show()


def display_nx_graph(graph: nx.Graph, filename: str = ""):
    nx.draw(graph, with_labels=True)
    plt.draw()
    if filename:
        plt.savefig(filename)
    plt.show()


def display_nx_digraph(graph: nx.DiGraph, filename: str = ""):
    pos = nx.shell_layout(graph)
    nx.draw(graph, pos, node_size=1000, with_labels=True, connectionstyle='arc3, rad = 0.25')
    plt.draw()
    if filename:
        plt.savefig(filename)

    plt.show()


def display_weighted_nx_di_graph(graph, filename: str = ""):
    pos = nx.shell_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.15)
    if filename:
        plt.savefig(filename)
    plt.show()


def display_flow_network(graph: nx.DiGraph, filename: str = ""):
    pos = nx.multipartite_layout(graph, subset_key="layer")
    colors = nx.get_edge_attributes(graph, 'color').values()
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, edge_color=colors, with_labels=True)
    plt.axis("equal")
    if filename:
        plt.savefig(filename)
    plt.show()
