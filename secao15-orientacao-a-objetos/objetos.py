class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id


lamp1 = Lampada("Branca", 110, 60)

print(lamp1.__dict__)


print(f"A lampada está ligada? {lamp1.checa_lampada()}")

lamp1.ligar_desligar()

print(f"A lampada está ligada? {lamp1.checa_lampada()}")


cc1 = ContaCorrente(4000, 20000)

user1 = Usuario("Vini", "Lenci", "vini@gmail.com", "123456")
