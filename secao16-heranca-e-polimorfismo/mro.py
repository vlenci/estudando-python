# Method Resolution Order (MRO)
# A ordem em que os métodos vão ser executados


class SerVivo:
    def mover(self):
        print("SerVivo: me movo de alguma forma.")


class Terrestre(SerVivo):
    def mover(self):
        print("Terrestre: ando com as pernas.")


class Aquatico(SerVivo):
    def mover(self):
        print("Aquatico: nado com nadadeiras.")


class Sapo(Terrestre, Aquatico):  # Essa ordem importa para o MRO
    pass


s = Sapo()
s.mover()
print(Sapo.__mro__)
