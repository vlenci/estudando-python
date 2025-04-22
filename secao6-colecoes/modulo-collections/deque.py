from collections import deque

# Criando deques

deq = deque("Lenci")
print(deq)

# Adicionando elementos
deq.append("x")
print(deq)

deq.appendleft("V")
print(deq)

# Remover elementos
deq.pop()
print(deq)

deq.popleft()
print(deq)