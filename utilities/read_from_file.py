from collections import defaultdict


def adjacency_matrix_from_file(file_name: str) -> list:
    """
        adjacency_matrix_from_file method reads adjacency matrix from file
        operated file format is:
        each lines contains one row with values separated by empty spaces

        examle:

        0 1 0
        1 0 1
        0 1 0
    """
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
    """
        incidence_matrix_from_file method reads incidence matrix from file
        operated file format is:
        each lines contains one row with values separated by empty spaces

        example:

        1 0
        1 1
        0 1
    """
    return adjacency_matrix_from_file(file_name)


def adjacency_list_from_file(file_name: str) -> defaultdict:
    """
        adjacency_list_from_file method reads adjacency list from file
        operated file format is:
        each lines contains node numbers that have connection with
        values are separated by empty spaces
        first value in the row is number of current node

        example:

        for adjacency list:
        0: 1, 2
        1: 0, 2
        2: 0, 1

        file format:
        0 1 2
        1 0 2
        2 0 1
    """

    adj_list = defaultdict(list)
    count = 0
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            new_list = line.split(" ")
            node = int(new_list[0])
            new_list = [int(i) for i in new_list[1:]]
            adj_list[node] = new_list

    file.close()

    return adj_list
