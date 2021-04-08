from algorithms.Kosaraju_algorithm import component_list
from random_generation.graph_generators import generate_digraph_with_probability
from visualization.nx_graph import display_nx_digraph

if __name__ == "__main__":
    G = generate_digraph_with_probability(7, 0.2)
    display_nx_digraph(G)

    comp = component_list(G)
    for u, v in comp.items():
        print(v, end=" ")