# Tuplas são representadas por parênteses
# Tuplas são imutávfeis, ao se criar uma tupla ela não muda. 
# Toda operação em uma tupla gera uma nova tupla

# Isso É uma tupla
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

# Isso TAMBÉM é uma tupla
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Isso NÃO é uma tupla
tupla3 = (4)
print(tupla3)
print(type(tupla3))

# Agora sim é uma tupla, ou seja, o que define no código uma tupla é a vírgula
tupla4 = (4, )
print(tupla4)
print(type(tupla4))

# Desempacotamento de tupla
tupla = ("Sistemas de Informação", "Prog 1")
curso, disciplina = tupla

print(tupla)
print(curso)
print(disciplina)

tupla = ("Tes", "te") # Isso funciona porque basicamente estou criando novamente a 
#                        tupla e atribuindo novos valores

print(tupla)

# tupla1[0] = "oi" -> isso aqui dá erro, porque aí sim eu estou tentando mudar o valor da tupla.

# Iterando sobre tupla
for num in tupla1:
    print(num)

# Transformando algo em tupla
nome = "Vinícius Lenci"
tupla_nome = tuple(nome)

print(tupla_nome)
print(tupla_nome.count('c')) # Mesma função que usamos em Listas funciona para Tupla

# Nesse exemplo faz sentido usar tupla porque os meses do ano não mudam
meses = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

# Iterando na tupla
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Tuplas são mais rápidas e seguras do que listas -> Imutabilidade 
