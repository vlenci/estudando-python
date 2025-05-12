from datetime import datetime

from banco import Administrador, Conta


def main() -> None:
    admin = Administrador()

    while True:
        print("Selecione uma opção no menu: ")
        print("========")
        print("1 - Criar conta")
        print("2 - Efetuar saque")
        print("3 - Efetuar depósito")
        print("4 - Efetuar transferência")
        print("5 - Listar contas")
        print("6 - Sair do sistema")

        opcao = int(input())

        # Falta terminar a lógica das opções
        if opcao == 1:
            nome = input("Insira o nome do titular: ")
            email = input("Insira o e-mail do titular: ")
            cpf = input("Insira o cpf do titular: ")
            dt_nasc = input("Insira a data de nascimento (dd/mm/yyyy): ")
            dt_nasc_formatada = datetime.strptime(dt_nasc, "%d/%m/%Y").date()

            conta = admin.criar_conta(nome, email, cpf, dt_nasc_formatada)
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        else:
            print("Insira uma opção válida.")


if __name__ == "__main__":
    main()
