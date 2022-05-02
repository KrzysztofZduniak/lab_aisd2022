#!/bin/python3

from graph2 import MatrixGraph, ListGraph
from graph_generation import (
    make_dag,
    sort_top,
)
from utils import bench, make_plot


start = 200
end = 1000
step = 15
per_step = 1
matrix_times = []
list_times = []
data = range(start, end, step)

for n in data:
    print(n)
    for _ in range(per_step):
        G = MatrixGraph(n, directed=True)
        make_dag(G, 0.6)
        matrix_times.append(bench(sort_top, G))

        G = ListGraph(n, directed=True)
        make_dag(G, 0.6)
        list_times.append(bench(sort_top, G))
make_plot("Sortowanie topologiczne", "sort_top", data, matrix_times, list_times)
