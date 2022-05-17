from graph2 import MatrixGraph
import sys

sys.setrecursionlimit(10000)

def euler(G, C=[], v=0):
    for w, i in enumerate(G[v]):
        if i == 1:
            G[v][w] = 2
            G[w][v] = 2
            euler(G, C, w)
    C.append(v)


def euler_cycle(G, v=0):
    C = []
    visited = set()

    def euler_rec(G, v):
        w_list = []
        for i in range(len(G[v])):
            if G[v][i] == 1:
                w_list.append(i)
        for w in w_list:
            if (v, w) in visited:
                continue
            else:
                visited.add((v, w))
                euler_rec(G, w)
    euler_rec(G, v)
    C.append(v)


def hamilton(G):
    V = []

    def hamilton_inner(G, v=0):
        V.append(v)
        for w, i in enumerate(G[v]):
            if i == 1 and w not in V:
                if hamilton_inner(G, w):
                    return True

        if len(V) == len(G) and G[0][v] == 1:
            return True
        else:
            V.remove(v)
        return False

    if hamilton_inner(G):
        return V
    else:
        return None

# G = [
#     [0, 1, 1, 0, 0, 0],
#     [1, 0, 1, 1, 1, 0],
#     [1, 1, 0, 1, 1, 0],
#     [0, 1, 1, 0, 1, 1],
#     [0, 1, 1, 1, 0, 1],
#     [0, 0, 0, 1, 1, 0],
# ]

# result = hamilton(G)
# print(*list(map(lambda x: x + 1, result)))
