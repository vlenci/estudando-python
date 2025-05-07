import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2025, 8, 27)

# Delta de tempo "datetime.timedelta"
tempo_ate_aniversario = aniversario - data_hoje

print(type(tempo_ate_aniversario))

print(tempo_ate_aniversario)

print(tempo_ate_aniversario.days)

# Contagem regressiva de 10 segundos


def contagem_regressiva(segundos):
    fim = datetime.datetime.now() + datetime.timedelta(seconds=segundos)
    ultimo_segundo = None

    while True:
        agora = datetime.datetime.now()
        restante = fim - agora

        # Arredondar o número de segundos restantes
        segundos_restantes = int(restante.total_seconds())

        if segundos_restantes != ultimo_segundo:
            ultimo_segundo = segundos_restantes
            if segundos_restantes > 0:
                print(
                    f"Tempo restante: {datetime.timedelta(seconds=segundos_restantes)}"
                )
            else:
                break

    print("Tempo esgotado!             ")


# Exemplo de uso:
contagem_regressiva(10)
