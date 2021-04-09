from random_generation.graph_generators import generate_with_edges, generate_with_probability

if __name__ == "__main__":
    graph = generate_with_edges(7, 7)
    print(graph.math_repr)
    graph.display()

    graph = generate_with_probability(7, 0.5)
    print(graph.math_repr)
    graph.display()