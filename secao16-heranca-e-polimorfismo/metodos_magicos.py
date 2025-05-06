class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"Nome completo: {self.__nome} {self.__sobrenome}"

    def __str__(self):
        return self.__nome

    def __repr__(self):
        return f"{self.__nome}, {self.__cpf}"


pess1 = Pessoa("Vinícius", "Lenci", "123.456.675-44")

print(pess1)
