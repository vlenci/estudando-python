# Mapeamento de valores para função

import math

def area(r):
    """Calcula área de um círculo de raio r"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros, uma função e um iterável
# passa um valor de cada vez do iterável para dentro da função

areas = map(area, raios)
print(areas) # Não imprime a lista em si, apenas <map object at 0x00000155B23BBDC0>
print(type(areas))
print(list(areas))
print(list(areas)) # Imprime lista vazia, já que após usar a função map() ele zera.

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r **2), raios)))

# Mais um exemplo

cidades = [("Berlim", 29), ("Cairo", 36), ("Buenos Aires", 19)]

print(cidades)

celsius_para_farenheit = lambda dado: (dado[0], 9/5 * dado[1] + 32)
print(list(map(celsius_para_farenheit, cidades)))


