# Dicionários em Python são conhecidos como Mapas em outras linguagens

paises = {
    "br" : "Brasil",
    "eua" : "Estados Unidos", 
    "es" : "Espanha"
}

print(paises)
print(type(paises))

# Acessando elementos: como não são indexados, usamos a chave
print(paises["br"])
# print(paises["ru"]) Isso aqui daria erro "KeyError"

# Forma recomendada de acesso:
print(paises.get("es"))
print(paises.get("ru")) # Esse aqui não da erro, ele retorna "None"

print("br" in paises)
print("ru" in paises)
print("Brasil" in paises) # Não encontra valor, apenas chaves

# Tuplas são ótimas para serem chaves, já que elas são imutáveis
localidades = {
    (35.9903, 39.0244) : "Ecritório Tóquio", 
    (25.3345, 23.4444) : "Escritório São Paulo"
}

print(localidades)
print(type(localidades))

receita = {
    "jan": 100,
    "fev" : 160, 
    "mar" : 80
}

print(receita)

# Forma 1 de adicionar elemento em um dict (mais comum)
receita["abr"] = 240
print(receita)

# Forma 2 de adicionar elemento em um dict
mes_novo = {"mai": 300}
receita.update(mes_novo)
print(receita)

# Forma 1 - Modificando dados 
receita["abr"] = 77
print(receita)

# Forma 2 - Modificando dados
receita.update({"mai": 690})
print(receita)

#
# Em dicionários não podemos ter chaves REPETIDAS
#

# Forma 1 - Remover dados de dicionário
ret = receita.pop("mar")
print(ret)
print(receita)

# Forma 2 
del receita["fev"]
print(receita)
