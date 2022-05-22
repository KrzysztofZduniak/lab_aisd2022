from itertools import cycle
from algorytmy import euler, hamilton, euler_cycle
import networkx as nx
import matplotlib.pyplot as plt
from time import time
import os
import sys
import random
import pandas as pd

sys.setrecursionlimit(100000)


def egdes_reverse(G, a, b, c):

    G[a][b] = 1 - G[a][b]
    G[b][a] = 1 - G[b][a]

    G[a][c] = 1 - G[a][c]
    G[c][a] = 1 - G[c][a]

    G[b][c] = 1 - G[b][c]
    G[c][b] = 1 - G[c][b]


def make_undirected_graph(n, pr):
    full_edges = (n-1)*n/2
    G = [[0]*n for _ in range(n)]
    cycle = list(range(n))
    random.shuffle(cycle)
    for v, w in zip(cycle[:-1], cycle[1:]):
        G[v][w] = 1
        G[w][v] = 1
    G[cycle[-1]][cycle[0]] = 1
    G[cycle[0]][cycle[-1]] = 1
    current_edges = n
    expected_edges = pr*full_edges
    while current_edges < expected_edges:
        a, b, c = random.sample(cycle, 3)
        s = G[a][b] + G[a][c] + G[b][c]
        if s > 1:
            continue
        else:
            egdes_reverse(G, a, b, c)
        current_edges += 3-s
    return G


def measure_time(n, pr, tries, function):
    s = 0
    for i in range(tries):
        print(f"{n} Nodes   Attempt {i+1}/{tries}")
        G = make_undirected_graph(n, pr)
        start = time()
        function(G)
        end = time()
        s += end-start
    return s/tries


def draw_plot(nodes, eu, ha, title, start, end):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of nodes")
    plt.ylabel("Time [s]")
    plt.plot(nodes, eu, label="Euler cycle")
    plt.plot(nodes, ha, label="Hamilton Cycle")
    plt.legend(loc="upper left")
    plt.title(
        f"Euler cycle and first Hamilton cycle: {title}% edge probability")
    plt.xlim(start, end)
    os.makedirs(os.path.join("wykresy", "zadanie 1"), exist_ok=True)
    plt.savefig(os.path.join("wykresy", "zadanie 1", f'lin_{title}.png'))
    plt.yscale("log")
    plt.savefig(os.path.join("wykresy", "zadanie 1", f'log_{title}.png'))
    plt.clf()
