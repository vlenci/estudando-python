import time


# Generator
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)

# Generator Expression
gen_inicio = time.time()
ge2 = (num for num in range(1000000000))
gen_tempo = time.time() - gen_inicio

print(sum(ge2))

# Teste de velocidade - Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1000000000)))
gen_tempo = time.time() - gen_inicio

# Teste de velocidade - List Comprehension

list_incio = time.time()
print(sum([num for num in range(1000000000)]))
list_tempo = time.time() - list_incio

print(f"Generator Expression levou: {gen_tempo}")
print(f"List Comprehension levou: {list_tempo}")
