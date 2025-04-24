# Retorna o maior valor do iterável

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

dicionario = {"a": 94, "b": 33, "c": 44, "d": 2}
print(max(dicionario.values()))

print(max("Pedro", "Helter", "Julia", "Wesley", "Vinícius"))

# Retorna o menor valor do iterável

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

dicionario = {"a": 94, "b": 33, "c": 44, "d": 2}
print(min(dicionario.values()))

nomes = ["Pedro", "Helter", "Julia", "Wesley", "Vinícius"]

print(min(nomes))

# Exemplos diferentes

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))  # Tim

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 5},
    {"titulo": "Too old to rock in'roll, too young to die", "tocou": 32},
]

# Inicializa com a primeira música como a mais e a menos tocada
mais_tocada = musicas[0]
menos_tocada = musicas[0]

# Percorre a lista a partir da segunda música
for musica in musicas[1:]:
    if musica["tocou"] > mais_tocada["tocou"]:
        mais_tocada = musica
    if musica["tocou"] < menos_tocada["tocou"]:
        menos_tocada = musica

print("Mais tocada:", mais_tocada["titulo"])
print("Menos tocada:", menos_tocada["titulo"])
