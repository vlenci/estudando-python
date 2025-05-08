"""
Atribuição e retorno de valor na mesma expressão

variavel := expressao
"""

print(nome := "Vinícius Lenci")

# Forma tradicional
"""
cesta = []
fruta = input("informe a fruta: ")
while fruta != "jaca":
    cesta.append(fruta)
    fruta = input("informe a fruta: ")
"""

# Utilizando Walrus
cesta = []
while (fruta := input("Informe a fruta: ")) != "jaca":
    cesta.append(fruta)
