from csv import writer, DictWriter

# Usando writer
with open("filmes.csv", "w", newline="") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(["Titulo", "Genero", "Duração"])
    while filme != "sair":
        filme = input("Insira o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])


# Usando DictWriter
# Define os nomes das colunas
cabecalho = ["Titulo", "Genero", "Duracao"]

with open("filmes.csv", "w", newline="") as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)

    escritor_csv.writeheader()  # Escreve o cabeçalho no arquivo

    filme = None
    while filme != "sair":
        filme = input("Insira o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow(
                {"Titulo": filme, "Genero": genero, "Duracao": duracao}
            )
