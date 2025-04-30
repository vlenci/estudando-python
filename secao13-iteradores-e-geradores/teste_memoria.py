# Fibonacci usando lista
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b  # 'a' recebe 'b' / 'b' recebe 'a + b'
    return nums


for n in fib_lista(100000):  # 450 MB de memória
    print(n)


# Fibonacci usando generator
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(100000):  # 30 MB de memória
    print(n)
