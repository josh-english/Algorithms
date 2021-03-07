def selection_sort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i, len(array)):
            if A[j] < A[min]:
                min = j
        temp = A[i]
        A[i] = A[min]
        A[min] = temp


A = [5, 2, 4, 6, 1, 3]
print("Before Selection Sort:")
print(A)
selection_sort(A)
print("After Selection Sort:")
print(A)