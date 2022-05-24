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


def draw_plot(nodes, t50, title):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of nodes")
    plt.ylabel("Time [s]")
    plt.plot(nodes, t50, label="50%")
    #plt.plot(nodes, t70, label="70%")
    plt.legend(loc="upper left")
    plt.title(
        f"All {title} cycles")
    #plt.xlim(start, end)
    os.makedirs(os.path.join("wykresy", "zadanie 2"), exist_ok=True)
    plt.savefig(os.path.join("wykresy", "zadanie 2", f'lin_{title}.png'))
    plt.yscale("log")
    plt.savefig(os.path.join("wykresy", "zadanie 2", f'log_{title}.png'))
    plt.clf()


#eu = pd.read_csv(os.path.join("wykresy","zadanie 1","data_euler.csv"))
ham = pd.read_csv(os.path.join("wykresy","zadanie_2","data_hamilton_all.csv"))

draw_plot(ham["points"], ham["50"],
        "Hamilton")