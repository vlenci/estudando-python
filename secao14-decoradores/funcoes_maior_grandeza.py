from random import choice


# Higher Order Function (HOF)
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando
print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas
def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "Te amo "))

    return humor() + pessoa


print(cumprimento("Angelina"))
print(cumprimento("Maria"))


def faz_me_rir():
    def rir():
        return choice(("hahaha", "kkkkk", "LoL"))

    return rir


print(faz_me_rir())  # Veja o retorno para entender a diferença da função anterior
rindo = faz_me_rir()
print(rindo())
