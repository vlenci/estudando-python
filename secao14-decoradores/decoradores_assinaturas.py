# O args e kwargs evita de dar erro de quantidade de parâmetros


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f"Olá, eu sou o/a {nome}"


@gritar
def ordenar(principal, acompanhamento):
    return f"Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}"


print(saudacao("Angelina"))
print(ordenar("Picanha", "Batata Frita"))
