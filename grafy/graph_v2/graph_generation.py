from graph2 import ListGraph, MatrixGraph
from random import randint, sample
import networkx as nx
import heapq


def dag_fulfilment(G):
    max_edge_count = ((G.size-1)*G.size) / 2
    return G.edge_count / max_edge_count


def get_random_dag_edge(size):
    i = randint(0, size-2)
    return (i, randint(i+1, size-1))


def make_dag(G, pr):
    if G.edge_count != 0:  # ify tutaj też just in case - może oszczędzić problemów przy debugowaniu
        raise RuntimeError("G must be empty")
    if G.directed is False:
        raise RuntimeError("G must be directed")
    all_egdes = []
    for i in range(G.size):
        for j in range(i+1, G.size):
            all_egdes.append((i, j))
    max_edge_count = ((G.size-1)*G.size) / 2
    edges_list = sample(all_egdes, int(pr * max_edge_count))
    #G.add_edges_from_list(edges_list)
    G_nx = nx.Graph()
    # for v in G.nodes():
    #     for u in G.successors(v):
    #         G_nx.add_edge(v, u, weight=G.get_weight(v, u))
    G_nx.add_edges_from(edges_list)
    while not nx.is_connected(G_nx):
        edges_list = sample(all_egdes, int(pr * max_edge_count))
        #G.add_edges_from_list(edges_list)
        G_nx = nx.Graph()
        # for v in G.nodes():
        #     for u in G.successors(v):
        #         G_nx.add_edge(v, u, weight=G.get_weight(v, u))
        G_nx.add_edges_from(edges_list)
    G.add_edges_from_list(edges_list)


def sort_top(G):
    result = []
    visited = set()

    def sort_top_rec(v: int):
        if v in visited:
            return
        visited.add(v)
        for u in G.successors(v):
            sort_top_rec(u)
        result.append(v)
    for v in G.nodes():
        sort_top_rec(v)
    return list(reversed(result))


def make_undirected_graph(n, pr, t):
    G = nx.fast_gnp_random_graph(n, pr)
    while not nx.is_connected(G):
        G = nx.fast_gnp_random_graph(n, pr)
    if t == "matrix":
        G2 = MatrixGraph(n)
        for e in G.edges():
            G2.add_edge(*e, weight=randint(1, 1001))
    elif t == "list":
        G2 = ListGraph(n)
        for e in G.edges():
            G2.add_edge(*e, weight=randint(1, 1001))
    else:
        raise RuntimeError(f"Unknown graph type: {t}")
    return G2


# def make_mst_prev(G):
#     TV = {0}
#     T = []
#     while len(T) < G.size - 1:
#         w = None
#         e = None
#         for item in TV:
#             for element in G.successors(item):
#                 if element in TV:
#                     continue
#                 nw = G.get_weight(item, element)
#                 if w is None:
#                     w = nw
#                     e = (item, element)
#                 elif w > nw:
#                     w = nw
#                     e = (item, element)
#         if w is None:
#             raise RuntimeError("Graph is not conected")
#         TV.add(e[1])
#         T.append(e)
#     return T


# def make_mst(G):
#     if G.directed:
#         raise RuntimeError("Graph is directed")
#     TV = {0}
#     edges = {(0, x) for x in G.successors(0)}
#     T = []
#     while len(T) < G.size - 1:
#         w = None
#         e = None
#         for item, element in list(edges):
#             if element in TV:
#                 edges.remove((item, element))
#                 continue
#             nw = G.get_weight(item, element)
#             if w is None:
#                 w = nw
#                 e = (item, element)
#             elif w > nw:
#                 w = nw
#                 e = (item, element)
#         if w is None:
#             raise RuntimeError("Graph is not conected")
#         TV.add(e[1])
#         T.append(e)
#         edges.update((e[1], x) for x in G.successors(e[1]))
#     return T

# def make_mst3(G):
#     if G.directed:
#         raise RuntimeError("Graph is directed")
#     TV = {0}
#     edges = [(G.get_weight(0,x), 0, x) for x in G.successors(0)]
#     heapq.heapify(edges)
#     T = []
#     while len(T) < G.size - 1:
#         w = e0 = e1 = None
#         while True:
#             w, e0, e1 = heapq.heappop(edges)
#             if e1 not in TV:
#                 break
#         TV.add(e1)
#         T.append((e0,e1))
#         for x in G.successors(e1):
#             heapq.heappush(edges, (G.get_weight(e1,x),e1,x))
#     return T


def mst3(G):
    if G.directed:
        raise RuntimeError("Graph is directed")
    TV = {0}
    T = []
    edges = [(G.get_weight(0, x), 0, x) for x in G.successors(0)]
    heapq.heapify(edges)
    while len(T) < G.size - 1:
        w, v, u = heapq.heappop(edges)
        while u in TV:
            w, v, u = heapq.heappop(edges)
        TV.add(u)
        T.append((v, u))
        for i in G.successors(u):
            heapq.heappush(edges, (G.get_weight(u, i), u, i))
    return T
