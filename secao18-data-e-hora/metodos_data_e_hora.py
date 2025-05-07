# datetime_exemplos.py
import datetime

# Convertendo uma string em data com strptime()
data_txt = "07/05/2025"
data_convertida = datetime.datetime.strptime(data_txt, "%d/%m/%Y")
print("Data convertida:", data_convertida)

# Formatando uma data como string com strftime()
agora = datetime.datetime.now()
formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", formatada)

# Comparando duas datas com operadores relacionais
evento = datetime.datetime(2025, 6, 1)
if agora < evento:
    print("O evento ainda vai acontecer.")
else:
    print("O evento já passou.")


# Descobrindo o dia da semana com weekday()
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
hoje = datetime.date.today()
print("Hoje é:", dias_semana[hoje.weekday()])

import datetime


# Formata uma data exibindo o mês por extenso em português
def formatar_data_em_portugues(data):
    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]
    dia = data.day
    mes = meses[data.month - 1]  # -1 já que os indices da lista vão de 0 a 11
    ano = data.year
    return f"{dia} de {mes} de {ano}"


data = datetime.datetime(2025, 5, 7)
print(formatar_data_em_portugues(data))  # Saída: 7 de maio de 2025

# Trabalhar somente com hora

almoco = datetime.time(12, 0, 0)

print(f"Horário de almoço: {almoco}")
