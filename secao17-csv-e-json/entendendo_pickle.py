import pickle

# Dados que queremos salvar
filmes = [
    {"titulo": "Matrix", "genero": "Ficção Científica", "duracao": 136},
    {"titulo": "Titanic", "genero": "Romance", "duracao": 195},
    {"titulo": "Gladiador", "genero": "Ação", "duracao": 155},
]

# Salvando os dados no arquivo binário
with open("filmes.pickle", "wb") as arquivo:
    pickle.dump(filmes, arquivo)

print("Filmes salvos com sucesso!")

# Carregando os dados
with open("filmes.pickle", "rb") as arquivo:
    filmes_carregados = pickle.load(arquivo)

print("Filmes carregados:")
for filme in filmes_carregados:
    print(filme)
