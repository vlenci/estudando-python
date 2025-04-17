nome = "Vini Lenci"
print(type(nome))


caractere = "c"
print(type(caractere))  # Não existe tipo "char" em Python

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9]
# ['V', 'i', 'n', 'i', ' ', 'L', 'e', 'n', 'c', 'i']

print(nome[0:4])
print(nome[5:10])

# [  0   ,    1   ]
# ["Vini", "Lenci"]
print(nome.split()[0])
print(nome.split()[1])

# [::-1] -> Começar do primeiro, ir até o final e inverter
print("subi no onibus"[::-1])

print(nome.replace("i", "e"))
