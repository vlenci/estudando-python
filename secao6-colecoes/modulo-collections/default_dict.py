from collections import defaultdict

# OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros 
# e retornar valores

dicionario = defaultdict(lambda: 0)
dicionario["curso"] = "Prog em python: Essencial"

print(dicionario)

print(dicionario["outro"]) # KeyError no dicionário comum, mas aqui não.
                           # Ele cria a chave com valor do lambda 

print(dicionario)