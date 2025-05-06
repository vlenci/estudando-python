class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"A {self.__nome} faz {som}")


# Utilização do "super()"
class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


felix = Gato("Ahri", "Felino", "VL")

felix.faz_som("Miauuu")
