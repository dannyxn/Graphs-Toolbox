from algorithms.Bellman_Fords_algorithm import BellmanFordAlgorithm

if __name__ == "__main__":
    adj_matrix = [[0,2,2,0,0],
                  [0,0,4,0,0],
                  [0,0,0,2,4],
                  [4,0,0,0,0],
                  [0,2,0,2,0]
    ]

    x = BellmanFordAlgorithm(adj_matrix)
    x.all_shortest_paths(4)
