import random

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array)

bubbleSort(array)
print("Array ordenado com Bubble Sort:", array)
