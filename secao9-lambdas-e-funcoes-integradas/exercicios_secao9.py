# 🧠 Lambda
# Crie uma função lambda que receba dois números e retorne o maior deles.
# Use essa função para comparar diferentes pares de números.

compara = lambda x, y: x if x > y else y  # noqa: E731

print(compara(32312312, 51312))

# 🔄 Map
# Dada a lista de preços abaixo, use `map()` para aplicar um desconto de 10% em cada item.
precos = [100, 250, 75, 300, 120]
print(precos)

desconto = map(lambda preco: preco * 0.9, precos)

print(list(desconto))
