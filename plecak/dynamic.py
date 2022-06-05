import imp
from time import time
from class_item import Item
import random


def dynamic_knapsack(number_of_items, capacity, all_items):
    # wydaje mi się, że generowanie danych wejścioweych
    # trzeba robić poza funkcja, ale zostawiłem też tutaj
    # do debugowania
    tb = [[0 for _ in range(capacity + 1)] for _ in range(number_of_items + 1)]
    # uzupełnianie tablicy
    for i in range(1, number_of_items + 1):
        w_i = all_items[i - 1].weight
        for j in range(1, capacity + 1):
            if w_i > j:
                tb[i][j] = tb[i - 1][j]
                continue
            tb[i][j] = max(tb[i - 1][j], tb[i - 1][j - w_i] + all_items[i - 1].value)
    # szukanie rozwiązania
    result = []
    i = number_of_items
    j = capacity
    while tb[i][j] > 0:
        if tb[i][j] == tb[i - 1][j]:
            i -= 1
        else:
            # tb[i][j] = tb[i][j] - all_items[i - 1].value
            j -= all_items[i - 1].weight
            result.append(all_items[i-1])
            i -= 1
    s = 0
    for item in result:
        s+= item.value
    return (s, result)


def dynamic_measure_time(capacity, tries, number_of_items, end_range):
    s = 0
    r = 0
    for i in range(tries):
        print(f"{i+1}/{tries} attempt")
        items = [Item(random.randint(1, end_range), random.randint(
        1, end_range)) for _ in range(number_of_items)]
        start = time()
        r += dynamic_knapsack(len(items), capacity, items)[0]
        end = time()
        s += end - start
    return (r, s / tries)


def print_tb(tb):
    for x in tb:
        print(*x, sep="\t")


if __name__ == "__main__":
    print(*dynamic_knapsack(4, 8, 4))
