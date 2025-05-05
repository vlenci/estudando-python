# Analogia legal:
# Assim como criamos uma váriavel do tipo "list" e conseguimos fazer operações com ela,
# podemos criar também uma classe, definir as operações dela (métodos) e usá-la (objetos).


class Lampada:
    pass


class ContaCorrente:  # CamelCase para classes.
    pass


lamp = Lampada()

print(type(lamp))

# Todos os tipos de dados em Python no fundo são Classes!
print(help(int))
print(help(float))
