from collections import namedtuple

# Precisamos definir nomes e parâmetros
# Forma 1
cachorro = namedtuple("cachorro", "idade raca nome")

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple("cachorro", "idade, raca, nome")

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple("cachorro", ["idade", "raca", "nome"])

# Usando
ray = cachorro(idade=2, raca="Chow Chow", nome = "Ray")

# Acessando os dados
# Forma 1
print(ray)
print(ray[2])
print(ray[1])

#Forma 2 - a mió
print(ray.nome)
print(ray.raca)
