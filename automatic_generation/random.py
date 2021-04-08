from core.graph_representation import GraphRepresentation, GraphRepresentationType

from random import randint, random
from collections import defaultdict


def generated_to_adj_list(G):
    adj_list = defaultdict(list)
    for x,y in enumerate(G):
        y.sort()
        tmp_list = []
        for i in y:
            tmp_list.append(i-1)
        adj_list[x] = tmp_list
    return adj_list


def print_G(G):
    for x,y in enumerate(G):
        y.sort()
        z = ""
        for i in y:
            z+=str(i)+" "
        print(f"{x+1}. {z}")


def G_n_l(n,l):
    G = [[] for _ in range(n)]
    for _ in range(l):
        x = randint(0,n-1)
        y = randint(1,n)
        while True:
            if (y-1)!=x and y not in G[x]:
                break
            y = randint(1,n)
        G[x].append(y)
        G[y-1].append(x+1)
    return G



def G_n_p(n,p):
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            if random() < p:
                if i!=j:
                    G[i].append(j+1)
                    G[j].append(i+1)
    return G


