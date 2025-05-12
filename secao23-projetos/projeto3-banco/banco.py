from datetime import date
from typing import List


def formatar_preco(preco) -> str:
    return f"R${preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class Conta:
    __contador: int = 5000

    def __init__(self, nome: str, email: str, cpf: str, dt_nasc: date):
        self.__numero_conta: int = Conta.__contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__dt_nasc: date = dt_nasc
        self.__saldo: float = 0.0
        Conta.__contador += 1

    def __str__(self):
        return (
            f"Conta: {self.__numero_conta}\n"
            f"Titular da conta: {self.__nome}\n"
            f"E-mail: {self.__email}\n"
            f"CPF: {self.__cpf}"
            f"Data de Nascimento: {self.__dt_nasc}"
        )

    @property
    def numero_conta(self) -> int:
        return self.__numero_conta

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def dt_nasc(self) -> date:
        return self.__dt_nasc

    @property
    def saldo(self) -> float:
        return self.__saldo

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email: str) -> None:
        self.__email = novo_email

    @cpf.setter
    def cpf(self, novo_cpf: str) -> None:
        self.__cpf = novo_cpf

    @dt_nasc.setter
    def dt_nasc(self, novo_dt_nasc: date) -> None:
        self.__dt_nasc = novo_dt_nasc

    def saque(self, valor: float) -> None:
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"Saque de {formatar_preco(valor)} realizado com sucesso.")
                print(f"Saldo atual: {formatar_preco(self.__saldo)}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    def deposito(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {formatar_preco(valor)} realizado com sucesso.")
            print(f"Novo saldo: {formatar_preco(self.__saldo)}")
        else:
            print("Valor de depósito inválido.")

    def transferencia(self, conta_destino: "Conta", valor: float) -> None:
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                conta_destino.__saldo += valor
                print(
                    f"Transferência de {formatar_preco(valor)} realizada com sucesso."
                )
                print(f"Novo saldo: {formatar_preco(self.__saldo)}")
            else:
                print("Saldo insuficiente para transferência.")
        else:
            print("Valor de transferência inválido.")


class Administrador:
    def __init__(self):
        self.__contas: List[Conta] = []

    def criar_conta(self, nome: str, email: str, cpf: str, dt_nasc: date) -> Conta:
        conta = Conta(nome, email, cpf, dt_nasc)
        self.__contas.append(conta)
        return conta

    def listar_contas(self) -> None:
        print("Contas registradas no sistema:")
        for conta in self.__contas:
            print(conta)

    @property
    def contas(self) -> List[Conta]:
        return self.__contas.copy()  # retorna uma cópia para segurança
