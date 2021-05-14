from algorithms.ford_fulkerson_algorithm import FordFulkersonAlgorithm
from random_generation.graph_generators import FLowNetworkGenerator

if __name__ == "__main__":
    flow_network = FLowNetworkGenerator()
    G = flow_network.generate_flow_network(4)

    ford_fulkerson = FordFulkersonAlgorithm(G)
    print(len(G))

