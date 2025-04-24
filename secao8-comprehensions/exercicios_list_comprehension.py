# 🧩 Exercício – List comprehension com processamento
# Dada a lista de nomes abaixo, crie uma nova lista contendo as iniciais (primeira letra de cada nome)
# seguidas de ponto. Exemplo: "Ana" -> "A.", "Bruno" -> "B.", etc.

nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eva"]

nomes_iniciais = [nome[0] + '.' for nome in nomes]
print(nomes_iniciais)

# 🧩 Exercício – Filtros em list comprehension
# A partir da lista `numeros = list(range(20))`, crie uma nova lista apenas com os números pares.

numeros = list(range(20))
print(numeros)

numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)

# 🧩 Exercício – List comprehension com números e strings
# Dada a lista de números abaixo, crie uma nova lista onde cada número seja convertido
# em uma string no formato: "Número: X", sendo X o valor original.

numeros = [3, 7, 1, 9, 4]

numeros_string = ["Número: " + str(num) for num in numeros]
print(numeros_string)

# 🧩 Exercício – List comprehension com strings maiúsculas
# Dada a lista de frutas abaixo, crie uma nova lista com todas as frutas em letras maiúsculas,
# no formato: "FRUTA: NOME_DA_FRUTA".

frutas = ["maçã", "banana", "uva", "melancia", "kiwi"]
# Sua resposta aqui

frutas_maiuscula = ["FRUTA: " + fruta.upper() for fruta in frutas]
print(frutas_maiuscula)
