# Sintaxe List Comprehension:
# [dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


nome = "Vinícius Lenci"
print([letra.upper() for letra in nome])

amigos = ["pedro", "vini", "heltinho", "ju", "wewe"]
print([amigo.upper() for amigo in amigos])