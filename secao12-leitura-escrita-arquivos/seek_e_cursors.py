# O seek move o cursor para determinado lugar

arquivo = open("texto.txt")

print(arquivo.read())

arquivo.seek(0)

print(arquivo.read(20))

arquivo.seek(0)

print(arquivo.readline())

arquivo.seek(0)

qtd_de_linhas = len(arquivo.readlines())
print(qtd_de_linhas)

arquivo.seek(0)

arquivo.close()

# Não vai abrir porque está fechado
# arquivo.read()
