import random

def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

array = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array)

selectionSort(array)
print("Array ordenado com Selection Sort:", array)
