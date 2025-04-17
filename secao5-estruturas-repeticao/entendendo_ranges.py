# 1. range(stop): de 0 até stop - 1
for num in range(5):
    print(num, end=" ")
print("\n")

# 2. range(start, stop): de start até stop - 1
for num in range(2, 6):
    print(num, end=" ")
print("\n")

# 3. range(start, stop, step): pulando de step em step
for num in range(0, 10, 2):
    print(num, end=" ")
print("\n")

# 4. range com passo negativo (contagem regressiva)
for num in range(10, 0, -1):
    print(num, end=" ")
print("\n")

# 5. Converter range em lista
print(list(range(4)))  # Resultado: [0, 1, 2, 3]
