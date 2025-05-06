# "Super Classe" ou "Classe Mãe"


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"Nome completo: {self.__nome} {self.__sobrenome}"


# Quando uma classe é filha de outra ela herda TODOS os atributos e métodos


class Cliente(Pessoa):
    """Cliente é filho de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario é filho de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f"Nome completo: {self._Pessoa__nome} {self._Pessoa__sobrenome} / Matrícula: {self.__matricula}"

    # Name Mangling


cli1 = Cliente("Vinicius", "Lenci", "123.456.789-00", 3000)
func1 = Funcionario("Kelly", "Key", "132.465.798-22", 1234)

print(cli1.nome_completo())
print(func1.nome_completo())

print(cli1.__dict__)
print(func1.__dict__)
