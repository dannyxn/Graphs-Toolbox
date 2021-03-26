import matplotlib.pyplot as plt
import networkx as nx

from random_generation.graph_generators import generate_connected_graph

if __name__ == "__main__":
    G = generate_connected_graph(7, 8)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.draw()
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
