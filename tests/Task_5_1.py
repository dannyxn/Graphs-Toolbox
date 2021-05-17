from random_generation.graph_generators import FlowNetworkGenerator
from visualization.nx_graph import display_flow_network

if __name__ == "__main__":
    flow_network = FlowNetworkGenerator()
    G = flow_network.generate_flow_network(4)

    display_flow_network(G)
