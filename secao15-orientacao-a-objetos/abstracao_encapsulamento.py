class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}"
        )

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


# Testando
conta1 = Conta("Geek", 150.00, 1500)
conta2 = Conta("Vini", 100.00, 2000)


print(conta1.__dict__)
print(conta2.__dict__)


conta1.transferir(100, conta2)

print(conta1.__dict__)
print(conta2.__dict__)
