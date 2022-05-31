import matplotlib.pyplot as plt
import pandas as pd
import os

def draw_plot_variable_items(x_axis, y_axis_greedy, y_axis_dynamic):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of items")
    plt.ylabel("Time [s]")
    plt.plot(x_axis, y_axis_greedy, label="Greedy")
    plt.plot(x_axis, y_axis_dynamic, label="Dynamic")
    plt.legend(loc="upper left")
    plt.title("Const capacity")
    os.makedirs(os.path.join("wykresy", "capacity_const"), exist_ok=True)
    plt.savefig(os.path.join("wykresy", "lin_const_capacity.png"))
    plt.yscale("log")
    plt.savefig(os.path.join("wykresy", "log_const_capacity.png"))
    plt.clf()