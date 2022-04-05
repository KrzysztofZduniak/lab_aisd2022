from quick import quicksort
import matplotlib.pyplot as plt
import statistics
import random
import time


def a_shaped_list(n):
    A = []
    for i in range(n - 1, 0, -2):
        A.append(i)
    for i in range(0, n, 2):
        A.append(i)
    return A


def bench(sort, A, pivot):
    startTime = time.time()
    sort(A, pivot)
    return time.time() - startTime


middle = []
right = []
rand = []
n = list(range(1, 1000, 5))

for i in n:
    A = a_shaped_list(i)
    print(A)
    middle.append(bench(quicksort, A, lambda p, r: (p + r) // 2))
    # right.append(bench(quicksort, A, lambda _, r: r))

    # r = statistics.fmean(
    #     [bench(quicksort, A, lambda p, r: random.randint(p, r)) for _ in range(10)]
    # )
    # rand.append(r)
    # rand.append(bench(quicksort, A, lambda p, r: random.randint(p, r)))
#
#
# fig, ax = plt.subplots()
# ax.plot(n, right, label="klucz skrajnie prawy")
# ax.plot(n, middle, label="klucz środkowy")
# ax.plot(n, rand, label="klucz losowy")
# ax.set(xlabel="n", ylabel="time", title="QuickSort")
# ax.legend()
# plt.show()
