import matplotlib.pyplot as plt
import networkx as nx


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


def display_flow_network(graph: nx.DiGraph):
    pos = nx.multipartite_layout(graph, subset_key="layer")
    colors = nx.get_edge_attributes(graph, 'color').values()
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, edge_color=colors, with_labels=True)
    plt.axis("equal")
    plt.show()
