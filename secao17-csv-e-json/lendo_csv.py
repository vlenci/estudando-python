# O encoding que resolveu o erro
"""Forma que funciona mas não é o ideal.
with open("lutadores.csv", encoding="utf-8") as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(",")[3:]
    print(dados)

"""

from csv import reader, DictReader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula a primeira linha (já que é um "Iterator")
    for linha in leitor_csv:
        print(f"{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros")

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)  # Pula a primeira linha (já que é um "Iterator")
    for linha in leitor_csv:
        print(
            f"{linha['Nome']} nasció en {linha['País']} y tiene {linha['Altura (em cm)']} centímetros"
        )
