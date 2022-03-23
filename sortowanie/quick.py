import random


def qs(A, L, R, get_pivot):
    p = A[get_pivot(L, R)]
    l = L
    r = R
    while l <= r:
        while A[l] < p:
            l += 1
        while A[r] > p:
            r -= 1
        if l > r:
            break
        A[l], A[r] = A[r], A[l]
        l += 1
        r -= 1
    if L < r:
        qs(A, L, r, get_pivot)
    if l < R:
        qs(A, l, R, get_pivot)


def quicksort(A, get_pivot):
    qs(A, 0, len(A) - 1, get_pivot)
    return A


if __name__ == "__main__":
    A = [14, 3, 12, 4, 1, 5, 20, 17, 8, 10, 13, 18, 6, 16]
    # A = [7, 2, 5, 4, 6, 3, 8, 1, 9]
    print(quicksort(A, lambda p, r: (p + r) // 2))
    print(quicksort(A, lambda p, r: random.randint(p, r)))
    print(quicksort(A, lambda p, r: r))
