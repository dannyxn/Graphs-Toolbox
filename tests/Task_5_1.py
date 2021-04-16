from random_generation.graph_generators import FLowNetworkGenerator
from visualization.nx_graph import display_flow_network

if __name__ == "__main__":
    flow_network = FLowNetworkGenerator()
    G = flow_network.generate_flow_network(4)

    display_flow_network(G)
