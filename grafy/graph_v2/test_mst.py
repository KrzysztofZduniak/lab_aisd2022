from graph2 import MatrixGraph  # , ListGraph
from graph_generation import (
    mst3 as mst,
    sort_top2 as top,
)
import matplotlib.pyplot as plt
import networkx as nx


txt = open("mst_test.txt")
matrix = list(map(lambda x: list(map(int, x.split())), txt.readlines()))
undirected = MatrixGraph(len(matrix))
G = nx.Graph()
for v, row in enumerate(matrix):
    for w, val in enumerate(row):
        try:
            undirected.add_edge(v, w, weight=val)
        except RuntimeError:
            continue
        if val != 0:
            G.add_edge(v, w, pos=(v, w), weight=val)


t = mst(undirected)
print(t)

sum = 0
for v, w in t:
    sum += undirected.n_and_e[v][w]
print(sum)

pos = nx.spring_layout(G)
k = G.edge_subgraph(t)
labels = {e: G.edges[e]["weight"] for e in G.edges()}
plt.subplot(121)
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.subplot(122)
nx.draw_networkx(k, pos=pos, node_color="r")

# plt.show()
