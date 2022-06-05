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
    os.makedirs(os.path.join("plots", "capacity_const"), exist_ok=True)
    plt.savefig(os.path.join(
        "plots", "capacity_const", "lin_const_capacity.png"))
    plt.yscale("log")
    plt.savefig(os.path.join(
        "plots", "capacity_const", "log_const_capacity.png"))
    plt.clf()


def draw_plot_variable_capacity(x_axis, y_axis_greedy, y_axis_dynamic):
    plt.figure(figsize=(16, 9))
    plt.xlabel("Number of items")
    plt.ylabel("Time [s]")
    plt.plot(x_axis, y_axis_greedy, label="Greedy")
    plt.plot(x_axis, y_axis_dynamic, label="Dynamic")
    plt.legend(loc="upper left")
    plt.title("Const capacity")
    os.makedirs(os.path.join("plots", "items_const"), exist_ok=True)
    plt.savefig(os.path.join("plots", "items_const", "lin_const_items.png"))
    plt.yscale("log")
    plt.savefig(os.path.join("plots", "items_const", "log_const_items.png"))
    plt.clf()


df_greedy = pd.read_csv(os.path.join("greedy",
                                     "greedy_with_variable_items.csv"))
df_dynamic = pd.read_csv(os.path.join("dynamic",
                                      "dynamic_with_variable_items.csv"))

draw_plot_variable_items(
    df_greedy["points"], df_greedy["time"], df_dynamic["time"])

df_greedy = pd.read_csv(os.path.join("greedy",
                                     "greedy_with_variable_capacity.csv"))
df_dynamic = pd.read_csv(os.path.join("dynamic",
                                      "dynamic_with_variable_capacity.csv"))

draw_plot_variable_capacity(
    df_greedy["points"], df_greedy["time"], df_dynamic["time"])
