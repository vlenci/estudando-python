# OBS: existem duas formas de utilizar um módulo

# Forma 1 - Importando o módulo inteiro - Não recomendado
# import random # Guarda tudo em memória

# Para usar a função random do pacote random, usamos '.' separando
# print(random.random())

# Forma 2 - Mais eficiente
from random import random
from random import uniform
from random import randint
from random import choice
from random import shuffle

for i in range(3):
    print(random())  # Não é mais necessário o random.random()


for i in range(3):
    print(uniform(3, 7))  # Num. Aleatórios entre 3 e 6.999...

for i in range(6):
    print(randint(1, 61), end=", ")  # Pseudo-aleatório -> pode repetir

print("\n")

jogadas = ["Pedra", "Papel", "Tesoura"]

print(choice(jogadas))  # Escolhe elemento da lista

cartas = ["A", "2", "3", "4", "5", "6", "7", "Q", "J", "K"]

shuffle(cartas)

print(cartas)
