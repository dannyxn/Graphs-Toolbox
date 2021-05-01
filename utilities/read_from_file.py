from collections import defaultdict


def adjacency_matrix_from_file(file_name: str) -> list:
    matrix = []
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list = line.split(" ")
            new_list = [int(i) for i in new_list]
            matrix.append(new_list)

    file.close()

    return matrix


def incidence_matrix_from_file(file_name: str) -> list:
    return adjacency_matrix_from_file(file_name)


def adjacency_list_from_file(file_name: str) -> list:
    adj_list = defaultdict(list)
    count = 0
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list = line.split(" ")
            new_list = [int(i) - 1 for i in new_list]
            adj_list[count] = new_list
            count += 1

    file.close()

    return adj_list

