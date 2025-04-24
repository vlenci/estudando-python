# 🧩 Exercício 1 – List comprehension simples
# Crie uma lista contendo os quadrados dos números de 1 a 10.
# Exemplo de saída esperada: [1, 4, 9, ..., 100]

quad_list = []

for num in range(1,11):
    quad_list.append(num ** 2)

print(quad_list)




# 🧩 Exercício 2 – Tuplas
# Dado o seguinte código:
# pessoas = [("Ana", 25), ("Bruno", 30), ("Clara", 22)]
# Imprima somente os nomes das pessoas.

pessoas = [("Ana", 25), ("Bruno", 30), ("Clara", 22)]
i = 0

while i < len(pessoas):
    nome, idade = pessoas[i]
    print(nome)
    i += 1



# 🧩 Exercício 3 – Dicionários
# Crie um dicionário chamado `alunos` que contenha como chave o nome do aluno e como valor sua nota.
# Depois, imprima os alunos com nota maior ou igual a 7.

alunos = {
    "Maria": 8.5,
    "João": 6.0,
    "Paula": 9.0,
    "Lucas": 5.5
}
for aluno, nota in alunos.items():
    if nota >= 7:
        print(f"Aluno(a) {aluno} tem nota maior ou igual a 7")
    else:   
        print(f"Aluno(a) {aluno} tem nota menor que 7")



# 🧩 Exercício 4 – Conjuntos
# Dadas as listas:
# lista_a = [1, 2, 3, 4, 5]
# lista_b = [4, 5, 6, 7, 8]
# Use conjuntos para encontrar os números em comum entre lista_a e lista_b.

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)

conjunto_comum = conjunto_a.intersection(conjunto_b)
print(conjunto_comum)

