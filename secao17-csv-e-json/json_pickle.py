# JSON -> JavaScript Object Notation

import json
import jsonpickle

# Mostrando a diferença de aspas no dict e no JSON
dicionario = {"teste": 123, "oi": 456}

print(dicionario)

print(json.dumps(dicionario))

# Criando JSON
ret = json.dumps(["produto", {"PlayStation 4": ("2TB", "Novo", "220V", 2340)}])

print(type(ret))

print(ret)

# Convertendo JSON para JSONPickle
"""
with open("produtos.json", "a+") as arquivo:
    ret_pickle = jsonpickle.encode(ret)
    arquivo.write(ret_pickle)
"""

with open("produtos.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret_read = jsonpickle.decode(conteudo)
    print(ret_read)
    print(type(ret_read))
