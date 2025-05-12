from datetime import date
from typing import List, Dict


def formatar_preco(preco) -> str:
    return f"R${preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class Produto:
    __id_contador = 0

    def __init__(
        self, nome: str, tipo: str, validade: date, qtd_estoque: int, preco: float
    ):
        self.__id = Produto.__id_contador
        Produto.__id_contador += 1

        self.__nome: str = nome
        self.__tipo: str = tipo
        self.__validade: date = validade
        self.__qtd_estoque: int = qtd_estoque
        self.__preco: float = preco
        self.__is_vencido: bool = False if validade > date.today() else True

    def __eq__(self, value):
        return isinstance(value, Produto) and self.id == value.id

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self) -> int:
        return self.__id

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
    def qtd_estoque(self) -> int:
        return self.__qtd_estoque

    @property
    def preco(self) -> int:
        return self.__preco

    @property
    def is_vencido(self) -> bool:
        return self.__is_vencido

    @is_vencido.setter
    def is_vencido(self, novo_is_vencido: bool) -> None:
        self.__is_vencido = novo_is_vencido

    @qtd_estoque.setter
    def qtd_estoque(self, nova_qtd_estoque: int) -> None:
        self.__qtd_estoque = nova_qtd_estoque


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
            if produto.is_vencido:
                self.produtos.remove(produto)

    def remover_produto(self, id: int) -> None:
        for produto in self.produtos:
            if produto.id == id:
                self.produtos.remove(produto)
                print(f"Produto com ID '{id}' removido do estoque com sucesso!")
                return
        print(f"Falha na remoção: Não existe produto com o ID '{id}' no estoque.")

    # Os print's estão com a formatação melhorada para facilitar visualização
    def visualizar_estoque(self):
        print("--- Estoque do Mercado MiCi ---")
        print(
            f"{'ID':<5} {'Nome':<20} {'Tipo':<15} {'Validade':<12} {'Quantidade':<13} {'Preço (unidade)':<10}"
        )
        print("-" * 90)

        for produto in self.produtos:
            validade_formatada = produto.validade.strftime("%d/%m/%Y")
            preco_formatado: str = formatar_preco(produto.preco)
            print(
                f"{produto.id:<5} {produto.nome:<20} {produto.tipo:<15} {validade_formatada:<12} {produto.qtd_estoque:<13} {preco_formatado:<10}"
            )


class Carrinho:
    def __init__(self):
        # Chave: Produto, Valor: Quantidade de produtos no carrinho
        self.__produtos_carrinho: Dict[Produto, int] = {}
        self.__total_pedido: float = 0.0

    @property
    def produtos_carrinho(self) -> Dict[Produto, int]:
        return self.__produtos_carrinho

    def adicionar_produto(self, produto: Produto) -> None:
        if produto in self.produtos_carrinho and produto.qtd_estoque > 0:
            self.produtos_carrinho[produto] += 1
        elif produto not in self.produtos_carrinho and produto.qtd_estoque > 0:
            self.produtos_carrinho[produto] = 1
        produto.qtd_estoque -= 1

    def remover_produto(self, produto: Produto) -> None:
        if self.produtos_carrinho[produto] > 1:
            self.produtos_carrinho[produto] -= 1
            produto.qtd_estoque += 1
        elif self.produtos_carrinho[produto] <= 1:
            del self.produtos_carrinho[produto]
            produto.qtd_estoque += 1
        else:
            print("O produto não está no carrinho")

    def visualizar_carrinho(self) -> None:
        print("--- Carrinho ---")
        print(
            f"{'ID':<5} {'Nome':<20} {'Tipo':<15} {'Validade':<12} {'Quantidade':<13} {'Preço':<10}"
        )
        print("-" * 85)

        for produto, quantidade in self.produtos_carrinho.items():
            if quantidade > 0:
                validade_formatada: str = produto.validade.strftime("%d/%m/%Y")
                preco_total = produto.preco * quantidade
                preco_formatado: str = formatar_preco(preco_total)
                print(
                    f"{produto.id:<5} {produto.nome:<20} {produto.tipo:<15} {validade_formatada:<12} {quantidade:<13} {preco_formatado:<10}"
                )

    def fechar_pedido(self) -> None:
        total_pedido = 0.0

        print("--- Resumo do pedido ---")
        print(
            f"{'ID':<5} {'Nome':<20} {'Tipo':<15} {'Validade':<12} {'Quantidade':<13} {'Preço':<10}"
        )
        print("-" * 85)

        for produto, quantidade in self.produtos_carrinho.items():
            validade_formatada: str = produto.validade.strftime("%d/%m/%Y")
            preco_total = produto.preco * quantidade
            preco_formatado: str = formatar_preco(preco_total)
            total_pedido += preco_total
            print(
                f"{produto.id:<5} {produto.nome:<20} {produto.tipo:<15} {validade_formatada:<12} {quantidade:<13} {preco_formatado:<10}"
            )

        total_formatado: str = formatar_preco(total_pedido)
        print("-" * 85)
        print(f"{'Total: ':>78}{total_formatado}")
