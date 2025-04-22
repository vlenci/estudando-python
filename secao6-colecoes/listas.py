lista1 = [1, 99, 33, 44, 66, 21, 89]

num = 40
if num in lista1:
    print(f"Encontrei o numero '{num}' na lista")
else:
    print(f"Não encontrei o número '{num}' da lista")


print("Lista original:\n", lista1)
lista1.append([1, 2, 3])  # Adiciona como lista
print("\n")
print("Adicionando com append:\n", lista1)
lista1.extend([7, 77, 777])  # Adiciona elemento a elemento
print("\n")
print("Adicionando com extend:\n", lista1)


print("\n")


nome = list("Vinícius ")
sobrenome = list("Lenci")
nome_completo = nome + sobrenome


print(nome_completo)

# nome[começo : fim: passo]
print(nome[7::-1])


lista2 = [1, 2, 3, 4]
print(lista2)

# Remove elemento da lista
lista2.pop()
print(lista2)

lista2.pop(1)
print(lista2)

lista3 = lista2 * 3
print(lista3)


curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)
curso = ' :D '.join(curso) # Pega a lista coloca ' :3 ' entre os elementos e monta uma string
print(curso)

# Exemplo de carrinho de mercado
carrinho = []
produto = ""

while produto != "sair":
    produto = input("Digite o nome do produto ou 'sair' para encerrar compra: ")
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print(carrinho)

# Utilizando variáveis em lista
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 6
num2 = 7
num3 = 8
num4 = 9
num5 = 10

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Só pra revisar o enumerate, que pode ser útil em listas muito longas, acaba "simulando" um BD
for indice, numero in enumerate(numeros):
    print(indice, numero)


muitos_numeros = []
for numero in range(0, 100000, 50):
    muitos_numeros.append(numero)

# Encontra em qual índice está o valor dentro do "()"
print(muitos_numeros.index(15600))

# Revisão de slicing
print(muitos_numeros[:10]) # Começa no incíce 0 e vai até o 10 - 1

# Algumas funções para lista de números
print(sum(muitos_numeros))
print(max(muitos_numeros))
print(min(muitos_numeros))
print(len(muitos_numeros))

# Copiando uma lista para outra
# Agora as listas são totalmente independentes, modificando uma não afeta a outra
# É chamado de Deep Copy .copy()
lista4 = [1, 2, 3]
print(lista4)

lista4_nova = lista4.copy()

print(lista4_nova)

lista4_nova.append(4)

print(lista4)
print(lista4_nova)

# Listas são dependentes lista1 = lista 2, ao modificar uma você modifica a outra também
# Shallow copy
lista5 = ['a', 'b', 'c']
print(lista5)

lista5_nova = lista5

print(lista5_nova)

lista5.append('d')

print(lista5)
print(lista5_nova)