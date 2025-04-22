from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos lista
lista = [1, 1, 1, 2, 2, 2, 3, 1, 1, 44, 42, 4, 4, 4, 1, 2, 777]

res = Counter(lista)

print(type(res))
print(res)


print(Counter("subinoonibus"))

# Pega as palavras de um texto e conta a quantidade de cada palavra
texto = "Claro! Aqui vai um exemplo simples e didático em Python para mostrar os diferentes tipos de collections: listas, tuplas, dicionários e conjuntos. Cada tipo é usado de uma maneira diferente, e vou explicar com comentários no código:"

palavras = texto.split()

res2 = Counter(palavras)

print(res2)
print(res2.most_common(3))