with open('loremipsum.txt', 'r') as file:
    content = file.read()

print("Conteúdo do arquivo:")
print(content)

with open('loremipsum.txt', 'r') as file:
    first_line = file.readline()

print("\nPrimeira linha do arquivo:")
print(first_line)

with open('loremipsum.txt', 'r') as file:
    file_content = file.read(3)

print("\nPrimeiros 3 caracteres do arquivo:")
print(file_content)

with open('loremipsum.txt', 'r') as file:
    content_with = file.read()

print("\nConteúdo do arquivo (usando 'with'):")
print(content_with)
