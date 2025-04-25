# Dicas de quando e onde tratar código:
# TODA ENTRADA deve ser tratada!
# Entrada do usuário principalmente - a função do usuário é DESTRUIR seu sistema

# else -> só é executado se não ocorrer o(s) erros

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Você digitou: {num}")
finally:
    print("Finally executado")

# O finally SEMPRE é executado
# Geralmente utilizado para desalocar recursos


# Exemplo 2


def dividir(a, b):
    return a / b


num1 = int(input("Informe o primeiro número: "))

try:
    num2 = int(input("Informe o segundo número: "))
except ValueError:
    print("O valor precisa ser numérico")

try:
    print(dividir(num1, num2))
except ValueError:
    print("O valor precisa ser numérico")


# Exemplo 2


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Não é possível dividir por 0"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))


# Exemplo 3


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f"Ocorreu um problema {err}")


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))
