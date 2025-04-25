# raise -> lança exceções

cores = ["azul", "verde", "marelo"]


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto precis ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")
    print(f"O texto {texto} será impresso na cor {cor}")


colore("Geek", "Azul")

colore("Geek", 10)
