from datetime import date
from typing import List


class Produto:
    def __init__(self, nome: str, tipo: str, validade: date, qtd_estoque: int):
        self.__nome: str = nome
        self.__tipo: str = tipo
        self.__validade: date = validade
        self.__qtd_estoque: int = qtd_estoque

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def validade(self) -> date:
        return self.__validade

    @property
    def qtd_estoque(self) -> date:
        return self.__qtd_estoque


class Estoque:
    def __init__(self):
        self.__produtos: List[Produto] = []

    @property
    def produtos(self) -> List[Produto]:
        return self.__produtos

    def cadastrar_produto(self, produto: Produto) -> None:
        self.produtos.append(produto)

    def remover_vencido(self) -> None:
        for produto in self.produtos:
            if produto.validade < date.today():
                self.produtos.remove(produto)

    def remover_estoque(self) -> None:
        self.produtos.qt

    # Os print's estão com a formatação melhorada para facilitar visualização
    def listar_estoque(self):
        print("Estoque do Mercado MiCi")
        print(f"{'Nome':<20} {'Tipo':<15} {'Validade':<12} {'Quantidade':<10}")
        print("-" * 60)

        for produto in self.produtos:
            validade_formatada = produto.validade.strftime("%d/%m/%Y")
            print(
                f"{produto.nome:<20} {produto.tipo:<15} {validade_formatada:<12} {produto.qtd_estoque:<10}"
            )


# LENCI DO PASSADO: FALTA COLOCAR QUANTIDADE DO PRODUTO NO CARRINHO
class Carrinho:
    def __init__(self):
        self.__produtos_carrinho: List[Produto] = []

    @property
    def produtos_carrinho(self) -> List[Produto]:
        return self.__produtos_carrinho

    def adicionar_produto(self, produto: Produto) -> None:
        self.produtos_carrinho.append(produto)
        produto.qtd_estoque -= 1

    def visualizar_carrinho(self) -> None:
        print("Carrinho")
        for produto in self.produtos_carrinho:
            print()
