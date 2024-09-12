with open('texto.txt', 'w') as file:
    texto = list()
    texto.append("Este é o primeiro texto.")
    texto.append("Este é o segundo texto.")
    texto.append("Este é o terceiro texto.")

    for linha in texto:
        file.write(linha + '\n')

print("Arquivo 'texto.txt' criado e preenchido.")
