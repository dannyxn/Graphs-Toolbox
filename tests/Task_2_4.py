from random_generation.euler_graph import generate_random_euler_graph


if __name__ == "__main__":
    graph = generate_random_euler_graph(8)
    print(graph)
    graph.display()