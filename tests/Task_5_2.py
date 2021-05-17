from algorithms.ford_fulkerson_algorithm import FordFulkersonAlgorithm
from random_generation.graph_generators import FlowNetworkGenerator
from visualization.nx_graph import display_flow_network

if __name__ == "__main__":
    flow_network = FlowNetworkGenerator()
    G = flow_network.generate_flow_network(5)

    display_flow_network(G)

    ford_fulkerson = FordFulkersonAlgorithm(G)

    print(ford_fulkerson.find_max_flow())

