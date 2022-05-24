from itertools import cycle
from algorytmy import euler, hamilton, euler_cycle
import networkx as nx
import matplotlib.pyplot as plt
from time import time
import os
import sys
import random
import pandas as pd
from functions import draw_plot, make_undirected_graph, measure_time, egdes_reverse

sys.setrecursionlimit(100000)


# def make_undirected_graphv3(n, pr):
#     G = nx.fast_gnp_random_graph(n, pr)
#     while not nx.is_eulerian(G):
#         G = nx.fast_gnp_random_graph(n, pr)
#     G2 = [[0]*n for _ in range(n)]
#     for e in G.edges():
#         G2[e[0]][e[1]] == 1
#     return G2





# def make_undirected_graph_2(n, pr):
#     G = nx.fast_gnp_random_graph(n, pr)
#     while not nx.is_eulerian(G):
#         G = nx.fast_gnp_random_graph(n, pr)
#     G2 = MatrixGraph(n)
#     for e in G.edges():
#         G2.add_edge(*e)
#     return G2



print("------------------------------------------------------\nHAMILTON CYCLE\n------------------------------------------------------")
start_nodes = int(input("Start nodes: "))
steps = int(input("Steps: "))
step_size = int(input("Step size: "))
tries = int(input("Tries: "))
end_elements = start_nodes + step_size*steps

x_axis = [x for x in range(start_nodes, end_elements, step_size)]
y_axis_30 = []
y_axis_70 = []

st = 1
for point in x_axis:
    print(f'Step {st}/{steps} {point} nodes {tries} tries')
    st += 1

    # pr = 0.3
    # y_axis_30.append(measure_time(point, pr, tries, hamilton))
    #y_axis_hamilton_30.append(measure_time(point, pr, tries, hamilton))

    pr = 0.7
    #y_axis_euler_70.append(measure_time(point, pr, tries, euler_cycle))
    y_axis_70.append(measure_time(point, pr, tries, hamilton))

#df = pd.DataFrame({"points":x_axis, "30": y_axis_30,"70": y_axis_70})
df = pd.DataFrame({"points":x_axis, "30": x_axis,"70": y_axis_70})
df.to_csv(os.path.join("wykresy", "zadanie_1", "data_hamilton.csv"))


# draw_plot(x_axis, y_axis_euler_30, y_axis_hamilton_30,
#           30, start_nodes, end_elements)
# draw_plot(x_axis, y_axis_euler_70, y_axis_hamilton_70,
#           70, start_nodes, end_elements)
