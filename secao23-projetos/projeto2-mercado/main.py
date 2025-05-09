from mercado import Produto, Estoque, Carrinho

from datetime import date, datetime


def cliente(estoque: Estoque) -> None:
    car = Carrinho()

    while True:
        print("Carrinho")
        print("========")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Visualizar carrinho")
        print("4 - Fechar pedido")
        print("5 - Cancelar compra")

        opcao = int(input())

        if opcao == 1:
            prod = input("Insira o nome do produto que deseja adicionar no carrinho: ")
            for produto in estoque.produtos:
                if produto.nome == prod:
                    car.adicionar_produto(produto)
                    print(f"'{prod}' adicionado com sucesso!")
                    print("\n")
                    break
            print(f"Não existe produto com nome '{prod}' no estoque.")
            print("")
        elif opcao == 2:
            prod = input("Insira o nome do produto que deseja remover do carrinho: ")
            for produto in car.produtos_carrinho:
                if produto.nome == prod:
                    car.remover_produto(produto)
                    print(f"Uma unidade de '{prod}' removida com sucesso!")
                    print("\n")
                    break
            else:
                print(f"O produto '{prod}' não está no carrinho.\n")

        elif opcao == 3:
            car.visualizar_carrinho()
            print("\n")
        elif opcao == 4:
            car.fechar_pedido()
            print("O mercado MiCi agradece sua preferência! Até logo.")
            break

        elif opcao == 5:
            break
        else:
            print("Insira uma opção válida.")


def administrador() -> None:
    est = Estoque()

    while True:
        print("Menu do Administrador")
        print("========================")

        print("1 - Cadastrar produto")
        print("2 - Remover produto")
        print("3 - Visualizar estoque")
        print("4 - Remover produtos vencidos")
        print("5 - Sair do sistema")
        print("")
        print("6 - Ir para menu do cliente")

        opcao = int(input())

        if opcao == 1:
            print("Cadastro de produto")
            print("===================")

            nome = input("Insira o nome do produto: ")
            tipo = input("Insira o tipo do produto: ")
            validade = input("Insira a validade do produto (dd/mm/yyyy): ")
            qtd_estoque = int(input("Insira a quantidade de produto no estoque: "))
            preco_unidade = float(input("Insira o preço unitário do produto: "))
            validade_convertida = datetime.strptime(validade, "%d/%m/%Y").date()

            prod = Produto(nome, tipo, validade_convertida, qtd_estoque, preco_unidade)
            est.cadastrar_produto(prod)

            print("\n")
        elif opcao == 2:
            print("Remoção de produto")
            print("==================")

            id_prod = int(input("Insira o ID do produto a ser removido: "))
            est.remover_produto(id_prod)
            print("\n")
        elif opcao == 3:
            est.visualizar_estoque()
            print("\n")
        elif opcao == 4:
            est.remover_vencido()
            print("Produtos vencidos removidos com sucesso!")
            print("\n")
        elif opcao == 5:
            break
        elif opcao == 6:
            cliente(est)
        else:
            print("Insira uma opção válida.")
            print("\n")


def main() -> None:
    administrador()


if __name__ == "__main__":
    main()
