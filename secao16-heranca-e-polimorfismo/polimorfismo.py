# Overwriting é uma das essencias do Polimorfismo


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar esse método")

    def comer(self):
        print(f"{self.__nome} está comento...")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.__nome} fala auau")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau")


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala ksksksks")


felix = Gato("Felix")
felix.comer()
felix.falar()

jerry = Rato("Jerry")
jerry.falar()
