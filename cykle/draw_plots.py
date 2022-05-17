from itertools import cycle
from algorytmy import euler, hamilton, euler_cycle
import networkx as nx
from graph2 import MatrixGraph
import matplotlib.pyplot as plt
from time import time
import os
import sys
import random
import pandas as pd
from functions import make_undirected_graph, measure_time, egdes_reverse

sys.setrecursionlimit(10000)


def draw_plot(nodes, t30, t70, title, start, end):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of nodes")
    plt.ylabel("Time [s]")
    plt.plot(nodes, t30, label="30%")
    plt.plot(nodes, t70, label="70%")
    plt.legend(loc="upper left")
    plt.title(
        f"Euler cycle and first Hamilton cycle: {title}% edge probability")
    plt.xlim(start, end)
    os.makedirs(os.path.join("wykresy", "zadanie 1"), exist_ok=True)
    plt.savefig(os.path.join("wykresy", "zadanie 1", f'lin_{title}.png'))
    plt.yscale("log")
    plt.savefig(os.path.join("wykresy", "zadanie 1", f'log_{title}.png'))
    plt.clf()


eu = pd.read_csv("data_euler.csv")
ham = pd.read_csv("data_hamilton.csv")

draw_plot(eu["points"], eu["30"], eu["70"],
          "Euler", eu["points"][0], eu["points"][-1])
draw_plot(ham["points"], ham["30"], ham["70"],
        "Hamilton", ham["points"][0], ham["points"][-1])