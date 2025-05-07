import math


# o MyPy acusa erro se tiver type hint em duas coisas ao mesmo tempo
# função e comentário
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(2))
