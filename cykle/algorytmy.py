def euler(G, C=[], v=0):
    for w, i in enumerate(G[v]):
        if i == 1:
            G[v][w] = 2
            G[w][v] = 2
            euler(G, C, w)
    C.append(v)


def hamilton(G):
    V = []
    end = False

    def hamilton_inner(G, v=0):
        V.append(v)
        for w, i in enumerate(G[v]):
            if i == 1 and w not in V:
                hamilton_inner(G, w)

        nonlocal end
        if not end:
            if set(V) == set(range(len(G))) and G[0][v] == 1:
                end = True
            else:
                V.remove(v)

    hamilton_inner(G)
    return V


def hamilton_all(G):
    solutions = []
    V = []

    def hamilton_inner(G, v=0):
        V.append(v)
        for w, i in enumerate(G[v]):
            if i == 1 and w not in V:
                hamilton_inner(G, w)

        if set(V) == set(range(len(G))) and G[0][v] == 1:
            solutions.append(V.copy())
        else:
            V.remove(v)

    hamilton_inner(G)
    return solutions


G = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]

result = hamilton(G)
print(*list(map(lambda x: x + 1, result)))
