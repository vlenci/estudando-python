# 1. Crie um programa que:
# a) Crie/abra um arquivo texto de nome “arq.txt”
# b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere “0”.
# c) Feche o arquivo
# d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.

with open("arq.txt", "w") as arquivo:
    while True:
        caractere = input("Insira caracteres ou '0' para sair: ")
        if caractere == "0":
            break
        arquivo.write(caractere)

arquivo = open("arq.txt")
print(arquivo.read())

# 2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.

nome_arquivo = input("Insira o nome do arquivo .txt: ")

with open(nome_arquivo, "r") as arquivo:
    texto = arquivo.read()
    lista_caracteres = list(texto)
    vogais = ["a", "e", "i", "o", "u"]
    qtd_vogais = 0
    qtd_consoantes = 0

    # "isalpha()" verifica se a string é apenas letras do alfabeto
    for caractere in lista_caracteres:
        if caractere.isalpha():
            if caractere.lower() in vogais:
                qtd_vogais = qtd_vogais + 1
            else:
                qtd_consoantes = qtd_consoantes + 1

    print(
        f"O arquivo de texto desejado tem {qtd_vogais} vogais e {qtd_consoantes} consoantes."
    )

# 3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este arquivo possui.

nome_arquivo = input("Insira o nome de um arquivo para contagem de linhas: ")

with open(nome_arquivo, "r") as arquivo:
    qtd_linhas = len(arquivo.readlines())

print(f"O arquivo desejado tem {qtd_linhas} linhas!")
