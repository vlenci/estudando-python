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
