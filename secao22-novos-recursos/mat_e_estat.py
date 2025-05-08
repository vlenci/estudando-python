import math
import statistics

nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}

# Produto de container numérico
print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))

print(math.isqrt(17))  # Devolve a parte inteira da raiz quadrada
print(math.sqrt(17))

# Distância euclidiana
ponto_3d_1 = (12, 40, 30)
ponto_3d_2 = [-23, 1, 22]

print(math.dist(ponto_3d_1, ponto_3d_2))

# Hipotenusa
# print(math.hypot(ponto_3d_1)) ERRO porque não descompactou a tupla com o '*'
print(math.hypot(*ponto_3d_1))


# Métodos estatísticos
seq1 = "Vinicius Lenci"
seq2 = [3, 2, 1, 4, 6, 3]
seq3 = [3, 2, 1, 3, 2, 1]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
