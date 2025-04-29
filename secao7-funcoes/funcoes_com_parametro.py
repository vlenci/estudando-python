def quadrado(numero):
    return numero**2


print(quadrado(3))
print(quadrado(4))

# print(quadrado(2, 3)) Isso daria ERRO, pois estou passando qtd
# diferente de parametros da função


def nome_completo(nome, sobrenome):
    return f"Seu nome completo é: {nome} {sobrenome}"


# A ordem dos argumentos importa!!
print(nome_completo("Vinícius", "Lenci"))

# As keywords previnem a ordem errada dos argumentos
print(nome_completo(sobrenome="Lenci", nome="Vinícius"))


# Erro comum: a posição do return
# Ao invés de somar todos os pares ele está retornando apenas
# a soma do primeiro número do laço
def soma_par():
    soma = 0
    for num in range(0, 10, 1):
        if num % 2 == 0:
            soma += num
        return soma


print(soma_par())
