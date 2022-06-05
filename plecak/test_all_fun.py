from greedy import greedy_knapsack
from dynamic import dynamic_knapsack
from class_item import Item
import random
from time import perf_counter
import multiprocessing

def do(x):
    number_of_items, capacity, tries, end_range_of_radnomization = x
    print(
        f"{number_of_items} items     {capacity} capacity     xd/{tries} attempt")
    all_items = [Item(random.randint(1, end_range_of_radnomization), random.randint(
        1, end_range_of_radnomization)) for _ in range(number_of_items)]

    start = perf_counter()
    params_dynamic = dynamic_knapsack(number_of_items, capacity, all_items)
    end = perf_counter()
    dyn_time = end-start
    

    start = perf_counter()
    params_greedy = greedy_knapsack(all_items, number_of_items, capacity)
    end = perf_counter()
    greedy_time = end-start
    
    return (params_dynamic[0], dyn_time, params_greedy[0], greedy_time)

def measure_parameters(number_of_items, capacity, tries, end_range_of_radnomization, pool):

    dyn_time = 0
    greedy_time = 0
    dyn_val = 0
    greedy_val = 0

    
    vals = pool.map(do, [(number_of_items, capacity, tries, end_range_of_radnomization)] * tries)
    dyn_time = sum(t[1] for t in vals)
    greedy_time = sum(t[3] for t in vals)
    dyn_val = sum(t[0] for t in vals)
    greedy_val = sum(t[2] for t in vals)

    dyn_time = dyn_time/tries
    greedy_time = greedy_time/tries

    error = (dyn_val-greedy_val)/dyn_val
    return (dyn_time, greedy_time, error)
