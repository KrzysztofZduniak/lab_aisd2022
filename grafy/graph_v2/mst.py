#!/bin/python3
from graph2 import MatrixGraph, ListGraph
from graph_generation import (
    make_undirected_graph,
    mst3 as mst,
)
from utils import bench, make_plot


start = 200
end = 1000
step = 15
per_step = 1
data = range(start, end, step)


def bench_mst(pr):
    matrix_times = []
    list_times = []
    for n in data:
        print(n)
        for _ in range(per_step):
            G = make_undirected_graph(n, pr, "matrix")
            matrix_times.append(bench(mst, G))

            G = make_undirected_graph(n, pr, "list")
            list_times.append(bench(mst, G))
    make_plot(
        f"Minimalne drzewo rozpinające (wypełnienie {pr*100}%)",
        f"sort_top_{pr*100}",
        data,
        matrix_times,
        list_times,
    )


bench_mst(0.3)
bench_mst(0.7)