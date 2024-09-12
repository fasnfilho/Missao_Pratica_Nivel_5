import random

array = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array)

array.sort()
print("Array ordenado (crescente):", array)

array.sort(key=None, reverse=True)
print("Array ordenado (decrescente):", array)

string_array = ["nome", "dataNascimento", "cpf", "rg"]
print("\nArray de strings original:", string_array)

string_array.sort()
print("Array de strings ordenado (crescente):", string_array)

string_array.sort(key=None, reverse=True)
print("Array de strings ordenado (decrescente):", string_array)
