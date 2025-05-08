# Jeito tradicional
def cumprimenta_v1(nome):
    return f"Olá {nome}!"


print(cumprimenta_v1("Lençote"))
print(cumprimenta_v1(nome="Lençote"))


# Obriga TODOS os argumentos que vem antes do '/' serem somente posicional
def cumprimenta_v2(nome, /):
    return f"Olá {nome}!"


print(cumprimenta_v2("Lençote"))
# print(cumprimenta_v2(nome="Lençote")) Esse aqui dá erro pq aceita somente argumentos posicionais


def cumprimenta_v3(*, nome):
    return f"Olá {nome}, tudo bem?"


# print(cumprimenta_v3("Lençola")) Isso aqui dá erro pq n tem o "nome=" antes
print(cumprimenta_v3(nome="Lençola"))
