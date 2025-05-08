from random import randint


class Calculadora:
    def __init__(self, dificuldade: int):
        self.__dificuldade: int = dificuldade
        self.__operacao: int = randint(1, 3)  # Soma: 1, Subtração: 2, Multiplicação: 3
        self.__valor1: int = self.gerar_valor
        self.__valor2: int = self.gerar_valor
        self.__resultado: int = self.gerar_resultado

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def resultado(self) -> int:
        return self.__resultado

    def __str__(self) -> str:
        op: str = ""

        if self.operacao == 1:
            op = "Soma"
        elif self.operacao == 2:
            op = "Subtração"
        elif self.operacao == 3:
            op = "Multiplicação"
        else:
            op = "Operador desconhecido"
        return f"Dificuldade: {self.dificuldade} \nPrimeiro Valor: {self.valor1} \nSegundo Valor: {self.valor2} \nOperação: {op} \nResultado: {self.resultado}"

    @property
    def gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(10, 100)
        elif self.dificuldade == 3:
            return randint(100, 1000)
        elif self.dificuldade == 4:
            return randint(1000, 10000)
        else:
            return 0

    @property
    def gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            return 0

    def checar_resultado(self, resposta: int) -> bool:
        if resposta == self.resultado:
            return True
        else:
            return False

    # parâmetro "pergunta": "antes" da pergunta ou "depois"
    def mostrar_operacao(self, pergunta: str = "antes") -> resultado:
        op: str = ""
        res: str | int
        if pergunta == "depois":
            res = self.resultado
        else:
            res = "?"

        if self.operacao == 1:
            op = "+"
        elif self.operacao == 2:
            op = "-"
        elif self.operacao == 3:
            op = "*"
        return f"{self.valor1} {op} {self.valor2} = {res}"
