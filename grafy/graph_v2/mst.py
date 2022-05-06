#!/bin/python3
import statistics
from graph2 import MatrixGraph, ListGraph
from graph_generation import (
    make_undirected_graph,
    mst3 as mst,
)
from utils import bench, make_plot


start = 600
end = 1500
step = 15
per_step = 3
data = range(start, end, step)


def bench_mst(pr):
    matrix_times = []
    list_times = []
    for n in data:
        print(n)
        matrix_one = []
        list_one = []
        for _ in range(per_step):
            G = make_undirected_graph(n, pr, "matrix")
            matrix_one.append(bench(mst, G))

            G = make_undirected_graph(n, pr, "list")
            list_one.append(bench(mst, G))
        matrix_times.append(statistics.mean(matrix_one))
        list_times.append(statistics.mean(list_one))
    make_plot(
        f"Minimalne drzewo rozpinające (wypełnienie {pr*100}%)",
        f"mst_{pr*100}_600",
        data,
        matrix_times,
        list_times,
    )


bench_mst(0.3)
bench_mst(0.7)
