from class_item import Item
import random


def dynamic_knapsack(
    number_of_items, capacity, end_range_of_radnomization, all_items=[]
):
    # wydaje mi się, że generowanie danych wejścioweych
    # trzeba robić poza funkcja, ale zostawiłem też tutaj
    # do debugowania
    if len(all_items) == 0:
        all_items = [
            Item(
                random.randint(1, end_range_of_radnomization),
                random.randint(1, end_range_of_radnomization),
            )
            for _ in range(number_of_items)
        ]
    tb = [[0 for _ in range(capacity + 1)] for _ in range(number_of_items + 1)]
    # uzupełnianie tablicy
    for i in range(1, number_of_items + 1):
        for j in range(1, capacity + 1):
            w_i = all_items[i - 1].weight
            if w_i > j:
                tb[i][j] = tb[i - 1][j]
                continue
            tb[i][j] = max(tb[i - 1][j], tb[i - 1][j - w_i] + all_items[i - 1].value)
    # szukanie rozwiązania
    result = []
    i = number_of_items
    j = capacity
    while j > 0 and i > 0:
        if tb[i][j] == tb[i - 1][j]:
            i -= 1
        else:
            tb[i][j] = tb[i][j] - all_items[i - 1].value
            j -= all_items[i - 1].weight
            result.append(i)
            i -= 1
    return result


def print_tb(tb):
    for x in tb:
        print(*x, sep="\t")


if __name__ == "__main__":
    print(*dynamic_knapsack(4, 8, 4))
