from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma = reduce(lambda acumulador, numero: acumulador + numero, numeros)

print(soma)
