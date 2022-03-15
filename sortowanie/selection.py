def selection(A):
    for j in range(len(A) - 1, 0, -1):
        max = j
        for i in range(j - 1, -1, -1):
            if A[i] > A[max]:
                max = i
        A[j], A[max] = A[max], A[j]
    return A
