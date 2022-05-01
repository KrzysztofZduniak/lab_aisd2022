import graph.graph as graph

def sort_top2(G):
    result = []
    visited = set()
    def sort_top2_rec(v: int):
        if v in visited:
            return
        visited.add(v)
        for u in G.successors(v):
            sort_top2_rec(u)
        result.append(v)
    for v in G.nodes():
        sort_top2_rec(v)
    return list(reversed(result))

def test_graph(G):
    print(sort_top2(G))
    print(f"{G.nodes()=}\n{G.successors(2)=}")

G = graph.MatrixGraph(4)
G.add_edges_from_list([(1, 2), (2,3), (0,2), (0,3), (1,3)])
test_graph(G)

G2 = graph.ListGraph(4)
G2.add_edges_from_list([(1, 2), (2,3), (0,2), (0,3), (1,3)])
test_graph(G2)