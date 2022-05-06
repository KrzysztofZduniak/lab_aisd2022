#!/bin/python3
import statistics
from graph2 import MatrixGraph, ListGraph
from graph_generation import (
    make_dag,
    sort_top2,
)
from utils import bench, make_plot


start = 500
end = 1500
step = 15
per_step = 3
matrix_times = []
list_times = []
data = range(start, end, step)

for n in data:
    print(n)
    matrix_one = []
    list_one = []
    for _ in range(per_step):
        G = MatrixGraph(n, directed=True)
        make_dag(G, 0.6)
        matrix_one.append(bench(sort_top2, G))

        G = ListGraph(n, directed=True)
        make_dag(G, 0.6)
        list_one.append(bench(sort_top2, G))
    matrix_times.append(statistics.mean(matrix_one))
    list_times.append(statistics.mean(list_one))
make_plot(f"Sortowanie topologiczne (wypełnienie 60%)", "sort_top", data, matrix_times, list_times)
