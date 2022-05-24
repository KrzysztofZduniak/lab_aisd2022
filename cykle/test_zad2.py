from itertools import cycle
from algorytmy import euler, hamilton, euler_cycle, hamilton_all
import networkx as nx
import matplotlib.pyplot as plt
from time import time
import os
import sys
import random
import pandas as pd
from functions import draw_plot, make_undirected_graph, measure_time, egdes_reverse

sys.setrecursionlimit(100000)
print("------------------------------------------------------\nHAMILTON CYCLE\n------------------------------------------------------")
start_nodes = int(input("Start nodes: "))
steps = int(input("Steps: "))
step_size = int(input("Step size: "))
tries = int(input("Tries: "))
end_elements = start_nodes + step_size*steps

x_axis = [x for x in range(start_nodes, end_elements, step_size)]
y_axis_50 = []
y_axis_70 = []

st = 1
for point in x_axis:
    print(f'Step {st}/{steps} {point} nodes {tries} tries')
    st += 1

    pr = 0.5
    y_axis_50.append(measure_time(point, pr, tries, hamilton_all))
    #y_axis_hamilton_30.append(measure_time(point, pr, tries, hamilton))

    # pr = 0.7
    # #y_axis_euler_70.append(measure_time(point, pr, tries, euler_cycle))
    # y_axis_70.append(measure_time(point, pr, tries, hamilton_all))

df = pd.DataFrame({"points": x_axis, "50": y_axis_50})
df.to_csv(os.path.join("wykresy", "zadanie_2", "data_hamilton_all.csv"))
