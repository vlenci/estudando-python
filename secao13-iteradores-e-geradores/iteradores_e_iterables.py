# Iterables
nome = "Vini"
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(type(it1))

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1)) -> Aqui daria erro "StopIterator" já que a string acaba e não tem mais iteravel

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
