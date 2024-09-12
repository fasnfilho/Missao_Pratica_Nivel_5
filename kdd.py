import time

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Leitura do arquivo e separação das palavras
words = []
with open('loremipsum.txt', 'r') as file:
    for line in file:
        words.extend(line.split())

print("Número de palavras:", len(words))

# Ordenação usando Bubble Sort
start_time = time.time()
bubbleSort(words)
bubble_sort_time = time.time() - start_time
print("Palavras ordenadas com Bubble Sort:", words)
print("Tempo de execução do Bubble Sort:", bubble_sort_time)

# Recarregar e ordenar usando Selection Sort
with open('loremipsum.txt', 'r') as file:
    words = []
    for line in file:
        words.extend(line.split())

start_time = time.time()
selectionSort(words)
selection_sort_time = time.time() - start_time
print("\nPalavras ordenadas com Selection Sort:", words)
print("Tempo de execução do Selection Sort:", selection_sort_time)

# Recarregar e ordenar usando método sort() do Python
with open('loremipsum.txt', 'r') as file:
    words = []
    for line in file:
        words.extend(line.split())

start_time = time.time()
words.sort()
python_sort_time = time.time() - start_time
print("\nPalavras ordenadas com sort() do Python:", words)
print("Tempo de execução do sort() do Python:", python_sort_time)

# Salvando as palavras ordenadas em um novo arquivo
with open('ordenado.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')

print("\nPalavras ordenadas salvas no arquivo 'ordenado.txt'.")
