nome = "Vinícius Lenci"

# Automaticamente a variável se torna um string de 1 caractere e vai printando até o "nome" acabar
for letra in nome:
    print(letra)

    
print(nome[0:8])

# Obviamente ele não vai até 300, ele para assim que acabar a lista de strings de 1 caractere
for letra in nome[9:300]:
    print(letra)

# Letra e indice da string
for valor in enumerate(nome):
    print(valor)

# Pega apenas a primeira parte (letra)
for _, valor in enumerate(nome):
    print(valor)
    
# Pega apenas a segunda parte (indice da letra)
for valor, _ in enumerate(nome):
    print(valor)    

# Para imprimir sem \n
for letra in nome:
    print(letra, end='')    


print("\n")


emoji = "\U0001F60D "
for num in range(1, 11):
    print(emoji * num)