def insertion_sort_decreasing(array):
    # account for zero-indexing
    for j in range(1, len(array)):
        key = array[j]
        # insert A[j] into the sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


A = [5, 2, 4, 6, 1, 3]
print("Before Insertion Sort:")
print(A)
insertion_sort_decreasing(A)
print("After Insertion Sort:")
print(A)