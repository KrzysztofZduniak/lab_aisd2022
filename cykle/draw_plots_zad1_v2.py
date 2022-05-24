from itertools import cycle
#from algorytmy import euler, hamilton, euler_cycle
import networkx as nx
import matplotlib.pyplot as plt
from time import time
import os
import sys
import random
import pandas as pd
#from functions import make_undirected_graph, measure_time, egdes_reverse

sys.setrecursionlimit(100000)


def draw_plot(nodes_eu, nodes_ham, eu, ham, title):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of nodes")
    plt.ylabel("Time [s]")
    plt.plot(nodes_eu, eu, label="Euler cycle")
    plt.plot(nodes_ham, ham, label="Hamilton cycle")
    plt.legend(loc="upper left")
    plt.title(
        f"Euler and first Hamilton cycle: {title}%")
    #plt.xlim(start, end)
    os.makedirs(os.path.join("wykresy", "zadanie_1"), exist_ok=True)
    plt.savefig(os.path.join("wykresy", "zadanie_1", f'lin_{title}.png'))
    plt.yscale("log")
    plt.savefig(os.path.join("wykresy", "zadanie_1", f'log_{title}.png'))
    plt.clf()


eu = pd.read_csv(os.path.join("wykresy", "zadanie_1", "data_euler.csv"))
ham = pd.read_csv(os.path.join("wykresy", "zadanie_1", "data_hamilton.csv"))

draw_plot(eu["points"], ham["points"], eu["30"], ham["30"],
         "30")
draw_plot(eu["points"],ham["points"], eu["70"], ham["70"],
          "70")