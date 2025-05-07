# Enunciado dos exercícios:
"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.

2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.

3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""


class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @marca.setter
    def marca(self, nova_marca: str) -> None:
        self.__marca = nova_marca

    @modelo.setter
    def modelo(self, nova_modelo: str) -> None:
        self.__modelo = nova_modelo

    def dados_veiculo(self) -> None:
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


astrinha = Veiculo("Chevrolet", "Astra")
astrinha.dados_veiculo()


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, nova_portas: int) -> None:
        self.__portas = nova_portas

    def dados_veiculo(self) -> None:
        super().dados_veiculo()
        print(f"Portas: {self.portas}")


polinho = Carro("Volksvawen", "Polo", 4)
polinho.dados_veiculo()
