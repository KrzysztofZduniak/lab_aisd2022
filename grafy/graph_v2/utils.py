import time
import matplotlib.pyplot as plt


def bench(f, G):
    start_time = time.time()
    f(G)
    end_time = time.time()
    return end_time - start_time


def make_plot(title, file_name, data, matrix_times, list_times):
    _, ax = plt.subplots()
    ax.plot(data, matrix_times, label="Macierz sąsiedztwa")
    ax.plot(data, list_times, label="Lista indydencji")
    ax.set(xlabel="n", ylabel="time", title=title)
    ax.legend()
    plt.savefig(f"wykresy/{file_name}.png")
