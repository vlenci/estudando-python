# Funções onde a passagem de parâmetro seja opcional

def quadrado(numero):
    return numero ** 2

print(quadrado(2))
# print(quadrado()) -> isso aqui iria dar TypeError, pq o parâmetro é obrigatório

# Agora o parâmetro "potencia" é opcional e por padrão vale 1
def exponencial(numero, potencia=1):
    return numero ** potencia

print(exponencial(2, 4))
print(exponencial(10))

# Exemplo de função como parâmetro
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, func=soma):
    return func(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(3, 4))
print(mat(3, 4, subtracao))

# Variável local e global

def diz_oi():
    nome = "Vinícius" # Var local
    return f"Ola {nome}"

print(diz_oi())
# print(nome) -> dá erro, já que a var "nome" é local

total = 0
def incrementa():
    global total # Obrigatório para usar var global dentro de função
    
    total = total + 1
    return total

print(incrementa())

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Necessário para usar variável que não é global, mas está na função de fora

        contador = contador + 1
        return contador
    return dentro()

print(fora())
# print(dentro()) -> da erro, já que é uma função local