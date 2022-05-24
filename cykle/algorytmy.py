import sys

sys.setrecursionlimit(100000)


def euler(G, C=[], v=0):
    for w, i in enumerate(G[v]):
        if i == 1:
            G[v][w] = 2
            G[w][v] = 2
            euler(G, C, w)
    C.append(v)


def euler_cycle(G, v=0):
    #t = 0
    C = []
    visited = set()

    def euler_rec(G, v):
        # nonlocal t
        # t += 1
        # print(f'{t=}')
        # w_list = []
        # for i in range(len(G[v])):
        for w, x in enumerate(G[v]):
            if x != 1:
                continue
            if v < w:
                if (v, w) in visited:
                    continue
                else:
                    visited.add((v, w))
            else:
                if (w, v) in visited:
                    continue
                else:
                    visited.add((w, v))
            euler_rec(G, w)
        C.append(v)
    euler_rec(G, v)
    return C


def hamilton(G):
    V = []

    def hamilton_inner(v=0):
        V.append(v)
        for w, i in enumerate(G[v]):
            if i == 1 and w not in V:
                if hamilton_inner(w):
                    return True

        if len(V) == len(G) and G[0][v] == 1:
            return True
        else:
            V.remove(v)
        return False

    if hamilton_inner():
        return V
    else:
        print("ERROR")
        quit()

def hamilton_all(G):
    V = []
    cycles = []

    def hamilton_inner(v=0):
        V.append(v)
        for w, i in enumerate(G[v]):
            if i == 1 and w not in V:
                hamilton_inner(w)

        if len(V) == len(G) and G[0][v] == 1:
            cycles.append(V[:])
        V.pop()

    hamilton_inner()
    return cycles

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
