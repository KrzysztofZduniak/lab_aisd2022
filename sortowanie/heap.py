def heap(A):
    build_heap(A)
    heapsize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        heapify(A, 0, heapsize)
    return A


def build_heap(A):
    heapsize = len(A)
    for i in range(len(A) // 2, -1, -1):
        heapify(A, i, heapsize)


def heapify(A, i, heapsize):
    l = (2 * i) + 1
    r = (2 * i) + 2
    print(f"i: {i}\tl:{l}\tr{r}")
    largest = None
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heapsize)

