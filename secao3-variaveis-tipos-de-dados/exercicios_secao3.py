print("1. Faça um programa que leia um número inteiro e imprima-o.")

# "Obriga" o número a ser inserido ser um inteiro, por conta da função "input()" receber tipo string
#  e não conseguir converter para int
num : int = int(input("Insira um número do tipo inteiro: "))


print(num)


print("2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.")


valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))


soma = valor1 + valor2 + valor3


print("A soma dos três valores é:", soma)


print("3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.")


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))


soma_dos_quadrados = valor1**2 + valor2**2 + valor3**2


print("A soma dos quadrados dos valores é:", soma_dos_quadrados)

