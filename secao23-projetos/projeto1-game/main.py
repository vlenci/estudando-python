from game import Calculadora


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    acumulado_pontos = pontos
    dificuldade = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: "))
    calc: Calculadora = Calculadora(dificuldade)

    print("Informe o resultado da seguinte operação: ")

    print(calc.mostrar_operacao(pergunta="antes"))

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        print("Resposta correta! :D")
        acumulado_pontos += 1
    else:
        print("Resposta incorreta! :(")

    print(calc.mostrar_operacao(pergunta="depois"))

    print("Deseja continuar no jogo? [1 - sim, 0 - não]")

    continuar_jogo = int(input())

    if continuar_jogo == 1:
        jogar(acumulado_pontos)
    if continuar_jogo == 0:
        print(f"Parabéns! Você fez um total de {acumulado_pontos} pontos!!")


if __name__ == "__main__":
    main()
