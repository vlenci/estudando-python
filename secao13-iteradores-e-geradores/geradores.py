# Generators são Iterators

# +------------------------+-------------------------+-------------------------------+
# | Característica         | Função Tradicional      | Generator (com yield)         |
# +------------------------+-------------------------+-------------------------------+
# | Palavra-chave usada    | return                  | yield                         |
# +------------------------+-------------------------+-------------------------------+
# | Retorno                | Valor único             | Um valor por vez (iterador)   |
# +------------------------+-------------------------+-------------------------------+
# | Estado mantido         | Não                     | Sim (pausa e continua do yield)|
# +------------------------+-------------------------+-------------------------------+
# | Memória usada          | Pode ser alta           | Baixa (lazy evaluation)       |
# +------------------------+-------------------------+-------------------------------+
# | Forma de uso           | resultado = f()         | for x in f():                 |
# +------------------------+-------------------------+-------------------------------+


# Generator Function (Não é um Generator, mas sim, ele gera um)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)
print(type(gen))
print(gen)

# Só dá algum retorno a partir de quando é iterado - motivo de ocupar menos memória
print(next(gen))
print(next(gen))
print(next(gen))

print("*separando*")

for num in gen:
    print(num)

# Observe que ao entrar no "for" ele não volta pro começo, mas continua a antiga iteração
