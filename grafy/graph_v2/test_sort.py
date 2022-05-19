from graph2 import MatrixGraph  # , ListGraph
from graph_generation import (
    sort_top2 as top,
)
import matplotlib.pyplot as plt
import networkx as nx


txt = open("topol_test.txt")
matrix = list(map(lambda x: list(map(int, x.split())), txt.readlines()))
directed = MatrixGraph(len(matrix), directed=True)
G = nx.DiGraph()
for v, row in enumerate(matrix):
    for w, val in enumerate(row):
        try:
            directed.add_edge(v, w, weight=val)
        except RuntimeError:
            continue
        if val != 0:
            G.add_edge(v, w, pos=(v, w), weight=val)


t = top(directed)
print(*t)


plt.plot()
nx.draw_networkx(G, with_labels=True)

plt.show()
