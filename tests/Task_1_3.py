from random_generation.graph_generators import generate_with_probability, generate_with_edges

if __name__ == "__main__":
    graph = generate_with_edges(10, 15)
    print(graph)
    graph.display()

    graph = generate_with_probability(7, 0.5)
    print(graph)
    graph.display()
