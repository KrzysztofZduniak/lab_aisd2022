from graph2 import MatrixGraph  # , ListGraph
from graph_generation import (
    mst3 as mst,
    sort_top2 as top,
)

txt = open("input")
n = txt.readline()
undirected = MatrixGraph(int(n))
directed = MatrixGraph(int(n), directed=True)
for v, row in enumerate(map(lambda x: list(x.split()), txt.readlines())):
    for w, val in enumerate(row):
        try:
            directed.add_edge(int(v), int(w), weight=int(val))
            undirected.add_edge(int(v), int(w), weight=int(val))
        except RuntimeError:
            continue

for x in undirected.n_and_e:
    print(*x)

mst(undirected)
top(directed)
