from random import random

# O retorno de uma função sem "return" é None

def hello_world():
    print("Hello World!")

ret_hel_wlrd = hello_world()

print(f"O retorno da função 'hello_world'é: {ret_hel_wlrd}")

# Função com retorno
def quadrado_de_7():
    return 7 * 7
    print("Essa linha NUNCA será executada!") # O "return" finaliza a função

print(f"O quadrado de 7 é: {quadrado_de_7()}")

# Uma função pode retornar vários valores:
# No fundo ela está retornando uma tupla que depois é desempacotada
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao  # retorna dois valores

# Chamando a função
resultado_soma, resultado_sub = operacoes(10, 5)

print("Soma:", resultado_soma)
print("Subtração:", resultado_sub)

def joga_moeda():
    valor = random() # Gera valores entre 0 e 1
    if valor > 0.5:
        return "Cara"
    return "Coroa" 

print(joga_moeda())
print(joga_moeda())
print(joga_moeda())
print(joga_moeda())

# Em uma função com apenas 2 retornos, é desnecessário usar o "else"
def eh_par(numero):
    if numero % 2 == 0:
        return "Par"
    return "Impar"

print(eh_par(4))
print(eh_par(5))
print(eh_par(-1))
