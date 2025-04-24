# Exemplo de len():

frases = [
    "Python é incrível",
    "List comprehension é poderosa",
    "Funções embutidas ajudam muito",
]

tamanhos = [len(frase.split()) for frase in frases]
print(tamanhos)

# Exemplo de sum():

alunos = {"Alice": [7.5, 8.0, 9.0], "Bruno": [6.0, 5.5, 7.0], "Carla": [9.5, 9.0, 10.0]}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno} - Média: {media}")

# Exemplo abs():

valores_reais = [100, 150, 200]
previsoes = [110, 140, 190]

erros = [abs(real - previsto) for real, previsto in zip(valores_reais, previsoes)]
print(erros)

# Exemplo round():

valores = [3.14159, 2.71828, 1.61803]
arredondados = [round(valor, 2) for valor in valores]
print(arredondados)
