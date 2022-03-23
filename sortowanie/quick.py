import random


def quicksort(A, get_pivot):
    qs(A, 0, len(A) - 1, get_pivot)
    return A


def qs(A, p, r, get_pivot):
    if p < r:
        q = partition(A, p, r, get_pivot)
        qs(A, p, q, get_pivot)  # left
        qs(A, q + 1, r, get_pivot)  # right


def partition(A, p, r, get_pivot):
    x = A[get_pivot(p, r)]
    i = p
    j = r
    while True:
        while A[j] > x:
            j = j - 1
        while A[i] < x:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            continue
        return j


if __name__ == "__main__":
    A = [14, 3, 12, 4, 1, 5, 20, 17, 8, 10, 13, 18, 6, 16]
    # A = [7, 2, 5, 4, 6, 3, 9, 1, 8]
    print(quicksort(A, lambda p, r: (p + r) // 2))
    # print(quicksort(A, lambda p, r: r))
    print(quicksort(A, lambda p, r: random.randint(p, r)))
