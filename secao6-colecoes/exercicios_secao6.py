# -----------------------------------------
# Exercício 1
# -----------------------------------------
print("1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.")

lista = []
for num in range(0, 6):
    lista.append(input(f"Insira o valor {len(lista) + 1}/6: "))
print(lista)

# -----------------------------------------
# Exercício 2
# -----------------------------------------
print("\n2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa deve executar os seguintes passos:")

# a)
print("a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.")

# b)
print("b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre na tela esta soma.")

# c)
print("c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.")

# d)
print("d) Mostre na tela cada valor da lista A, um em cada linha.")

A : list[int] = [1, 0, 5, -2, -5, 7]
soma : int = A[0] + A[1] + A[5]

print(f"A soma dos valores originais da lista é: {soma}")

A[5] = 100

"""
for num in A:
    print(A[num]) 
Aqui vai dar erro porque o "num" acessa o valor da lista
e não o indíce!
"""

for num in A:
    print(num) 

# -----------------------------------------
# Exercício 3
# -----------------------------------------
print("\n3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.")

# Código da lógica aqui...

n = 0
pares = 0
lista_ex3 = []

while n < 10: 
    valor = int(input(f"Insira o valor {n + 1}/10: "))
    lista_ex3.append(valor)
    n += 1

    if valor % 2 == 0:
        pares += 1
    
print(f"A lista apresenta {pares} números pares!")
        


