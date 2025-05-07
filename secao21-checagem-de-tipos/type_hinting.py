def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}!"


print(cumprimentar("Lençote"))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho("Lenci University"))

print(cabecalho("Lenci Univesity", False))
