import random
from class_item import Item
import pandas as pd
from test_all_fun import measure_parameters
import os
import multiprocessing

def main():
    test = int(input("Which would be NOT constant\n1- number of items\n2- Capacity\n"))
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
        x_axis = []
        for i in range(steps):
            x_axis.append(number_of_items+ step_size*i)
    else:
        end_elements = capacity + steps*step_size
        x_axis = []
        for i in range(steps):
            x_axis.append(capacity+ step_size*i)

    if test == 2:
        all_items = [Item(random.randint(1, end_range_of_radnomization), random.randint(
            1, end_range_of_radnomization)) for _ in range(number_of_items)]

    greedy_time = []
    dynamic_time = []
    error = []
    # greedy_values = []
    # dynamic_values = []

    st = 1
    with multiprocessing.Pool(processes=8) as pool:
        for point in x_axis:
            print(f"Step {st}/{steps}")
            st += 1
            if test == 1:
                params = measure_parameters(
                    point, capacity, tries, end_range_of_radnomization, pool)
            else:
                params = measure_parameters(
                    number_of_items, point, tries, end_range_of_radnomization, pool)
            greedy_time.append(params[1])
            dynamic_time.append(params[0])
            error.append(params[2])

    if test == 1:
        df_greedy = pd.DataFrame(
            {"points": x_axis, "time": greedy_time, "error": error})
        df_greedy.to_csv(os.path.join("greedy", "greedy_with_variable_items.csv"))
        df_dynamic = pd.DataFrame({"points": x_axis, "time": dynamic_time})
        df_dynamic.to_csv(os.path.join(
            "dynamic", "dynamic_with_variable_items.csv"))
    else:
        df_greedy = pd.DataFrame(
            {"points": x_axis, "time": greedy_time, "error": error})
        df_greedy.to_csv(os.path.join(
            "greedy", "greedy_with_variable_capacity.csv"))
        df_dynamic = pd.DataFrame({"points": x_axis, "time": dynamic_time})
        df_dynamic.to_csv(os.path.join(
            "dynamic", "dynamic_with_variable_capacity.csv"))

if __name__ == "__main__":
    main()