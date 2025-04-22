# ------------------------------------------------------
# DIFERENÇAS ENTRE dict E OrderedDict NO PYTHON ATUAL
# ------------------------------------------------------

from collections import OrderedDict

print("===== 1. ORDEM DE INSERÇÃO =====")

# Em versões modernas do Python (3.7+), dict já mantém a ordem
meu_dict = {"banana": 3, "maçã": 5, "laranja": 2}
print("dict comum:")
for fruta, quantidade in meu_dict.items():
    print(fruta, ":", quantidade)

# OrderedDict também mantém a ordem, mas isso já era garantido mesmo antes
meu_ordered_dict = OrderedDict()
meu_ordered_dict["banana"] = 3
meu_ordered_dict["maçã"] = 5
meu_ordered_dict["laranja"] = 2
print("\nOrderedDict:")
for fruta, quantidade in meu_ordered_dict.items():
    print(fruta, ":", quantidade)

# ------------------------------------------------------

print("\n===== 2. MÉTODO EXCLUSIVO DO ORDEREDDICT: move_to_end =====")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("Antes do move_to_end:", od)

# move 'a' para o final
od.move_to_end('a')
print("Depois de move_to_end('a'):", od)

# move 'b' para o início
od.move_to_end('b', last=False)
print("Depois de move_to_end('b', last=False):", od)

# ------------------------------------------------------

print("\n===== 3. COMPARAÇÃO ENTRE dict E OrderedDict =====")

# dict comum: a ordem não importa na comparação
d1 = {'x': 1, 'y': 2}
d2 = {'y': 2, 'x': 1}
print("dicts comuns iguais?:", d1 == d2)  # True

# OrderedDict: a ordem importa
od1 = OrderedDict([('x', 1), ('y', 2)])
od2 = OrderedDict([('y', 2), ('x', 1)])
print("OrderedDicts iguais?:", od1 == od2)  # False

# ------------------------------------------------------

print("\n===== 4. QUANDO USAR QUAL? =====")
print("""
- Use dict para praticamente tudo (Python 3.7+ já mantém a ordem).
- Use OrderedDict se você precisa de:
    • Métodos como move_to_end()
    • Comparações que considerem a ordem
    • Compatibilidade com versões antigas
""")
