from greedy import greedy_knapsack
from dynamic import dynamic_knapsack
from class_item import Item
import random
from time import perf_counter


def measure_parameters(number_of_items, capacity, tries, end_range_of_radnomization):

    dyn_time = 0
    greedy_time = 0
    dyn_val = 0
    greedy_val = 0

    for i in range(tries):
        print(
            f"{number_of_items} items     {capacity} capacity     {i+1}/{tries} attempt")
        all_items = [Item(random.randint(1, end_range_of_radnomization), random.randint(
            1, end_range_of_radnomization)) for _ in range(number_of_items)]

        start = perf_counter()
        params_dynamic = dynamic_knapsack(number_of_items, capacity, all_items)
        end = perf_counter()
        dyn_time += end-start
        dyn_val += params_dynamic[0]

        start = perf_counter()
        params_greedy = greedy_knapsack(all_items, number_of_items, capacity)
        end = perf_counter()
        greedy_time += end-start
        greedy_val += params_greedy[0]

    dyn_time = dyn_time/tries
    greedy_time = greedy_time/tries

    error = (dyn_val-greedy_val)/dyn_val
    return (dyn_time, greedy_time, error)
