print(
    "1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior."
)


numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais.")


print(
    "2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido."
)


import math

numero = int(input("Digite um número inteiro: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada do número é:", raiz)
else:
    print(
        "Número inválido. Não é possível calcular a raiz quadrada de número negativo."
    )


print(
    "3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar."
)


numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
