print(
    "Ex. 1: Faça um programa que determine e mostre os cinco primeiros"
    " múltiplos de 3, considerando números maiores que 0."
)


n = 0
for num in range(1, 100):
    if n < 5:
        if num % 3 == 0:
            print(num)
            n = n + 1


print(
    "2. Faça um programa que utilize o comando while para mostrar "
    "na tela uma contagem regressiva, iniciando "
    "em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem."
)


contador = 10

while contador >= 0:
    print(contador)
    contador = contador - 1
print("FIM!")


for numero in range(0, 100001, 1000):
    print(numero)
