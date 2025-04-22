# Faz referência a Teorioa dos Conjuntos na Matemática

# - Sets(conjuntos) não possuem valores duplicados
# - Sets(conjuntos) não possuem valores ordenados

# Diferença entre Conjuntos (sets) e Mapas (Dicionários) em Python
# - Um dicionário te chave/valor;
# - Um conjunto tem apenas valor;

# Definindo um conjunto
# Forma 1 
s = set({1, 2, 3, 4, 5, 5, 6, 7, 7, 2, 3}) # Os números repetidos são ignorados e não adicionados ao conjunto
print(s)
print(type(s))

s1 = {1, 2, 3, 4, 5, 3, 3, 8, 7, 6, 88, 5.5} # Os sets também NÃO tem ordem, ele faz como der na telha basicamente
print(s1)
print(type(s1))

# Um conjunto pode ter vários tipos de dados, assim como os outros tipos de collections
set_misturado = {1, 3, 2, "a", "c", "d", "c",}
print(set_misturado)

# Adicionar e remover valores
conjunto = {1, 2, 3, 4}
print(conjunto)
print(type(conjunto))

conjunto.add(5)
print(conjunto)

conjunto.remove(1)
print(conjunto)

# Metodos matemáticos em python
estudantes_ia = {"Jullia", "Guijas", "Lenci"}
estudantes_logica = {"Fernandinho", "Jullia", "José"}

# Mostra apenas os que não se repetem - Forma 1 (mais recomendada)
estudantes_unicos = estudantes_ia.union(estudantes_logica)
print(estudantes_unicos)

# Forma 2
estudantes_unicos_2 = estudantes_ia | estudantes_logica
print(estudantes_unicos_2)

# Os que estudam ambas as disciplinas - Forma 1 
ambos1 = estudantes_ia.intersection(estudantes_logica)
print(ambos1)

#Forma 2
ambos2 = estudantes_logica & estudantes_ia
print (ambos2)

# Gerar conjunto de estudantes que não estão no outro curso
apenas_ia = estudantes_ia.difference(estudantes_logica)
print(apenas_ia)

apenas_logica = estudantes_logica.difference(estudantes_ia)
print(apenas_logica)


