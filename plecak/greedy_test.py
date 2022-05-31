import random
from class_item import Item
import pandas as pd
from greedy import greedy_knapsack, measure_time_for_greedy, greedy_const, measure_time_const_items
import os

test = int(input("Which would be NOT constant\n1- number of items\n2-Capacity\n"))
while test != 1 and test != 2:
    test = int(
        input("TYPO\nWhich would be NOT constant\n1- number of items\n2- Capacity\n"))

if test == 1:
    number_of_items = int(input("START number of items: "))
    capacity = int(input("CONST capacity: "))
else:
    number_of_items = int(input("CONST Number of items: "))
    capacity = int(input("START capacity: "))


end_range_of_radnomization = int(
    input("End range of wieghts and values randomization: "))
steps = int(input("Steps: "))
step_size = int(input("Step size: "))
tries = int(input("Tries: "))

if test == 1:
    end_elements = number_of_items + steps*step_size
    x_axis = []
    for i in range(steps):
        x_axis.append(number_of_items*(i+1))
else:
    end_elements = capacity + steps*step_size
    x_axis = []
    for i in range(steps):
        x_axis.append(capacity*(i+1))

if test == 2:
    all_items = [Item(random.randint(1, end_range_of_radnomization), random.randint(
        1, end_range_of_radnomization)) for _ in range(number_of_items)]
    all_items.sort(key=lambda x: x.profit, reverse= True)

y_axis = []
st = 1
for point in x_axis:
    print(f'Step {st}/{steps} {tries} tries {point=}')
    st += 1
    if test == 1:
        y_axis.append(measure_time_for_greedy(
            point, capacity, end_range_of_radnomization, tries))
    else:
        y_axis.append(measure_time_const_items(
            all_items, number_of_items, point, tries))

if test == 1:
    df = pd.DataFrame({"points": x_axis, "time": y_axis})
    df.to_csv(os.path.join("wykresy", "greedy",
              "greedy_with_variable_items.csv"))
else:
    df = pd.DataFrame({"points": x_axis, "time": y_axis})
    df.to_csv(os.path.join("wykresy", "greedy",
              "greedy_with_variable_capacity.csv"))
