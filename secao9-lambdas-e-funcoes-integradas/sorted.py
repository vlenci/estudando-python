# O sort() só funciona em listas, já o "sorted()" funciona em qualquer iterável

numeros = (6, 1, 8, 2)
print(numeros)

sorted(numeros)  # Não vai funcionar. já que ele ordena e cria uma nova lista
# ele não modifica a lista existente

print(sorted(numeros))  # Aqui vai dar certo. SEMPRE transforma em lista

print(sorted(numeros, reverse=True))

# Ordenar pelo tamanho

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu sou sigma", "oi betas"]},
    {"username": "laurinha", "tweets": []},
    {"username": "ken", "tweets": []},
]

print(usuarios)

print(sorted(usuarios, key=lambda usario: usario["username"]))
