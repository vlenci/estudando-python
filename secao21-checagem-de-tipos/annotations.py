import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)

nome: str = "Vinícius Lenci"

ativo: bool = True

peso: float = 90.7

print(__annotations__)
