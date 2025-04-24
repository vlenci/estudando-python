lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Zip de listas
zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

print(list(zip1))

# Zip de tuplas
zip1 = zip(lista1, lista2)
print(tuple(zip1))

# Zip de conjuntos
zip1 = zip(lista1, lista2)
print(set(zip1))

# Zip de dicionários
zip1 = zip(lista1, lista2)
print(dict(zip1))

# Quando as coelções tem tamanhos diferentes, ela para de iterar na coleção de menor tamanho.
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
