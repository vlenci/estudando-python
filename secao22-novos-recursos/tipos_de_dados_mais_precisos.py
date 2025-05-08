from typing import Literal, Union, TypedDict, Protocol, Final, final


# Literal: aceita apenas valores específicos
def get_status_text(status: Literal["open", "closed"]) -> str:
    if status == "open":
        return "Está aberto"
    elif status == "closed":
        return "Está fechado"


# Teste do Literal
print(get_status_text("open"))  # Saída: Está aberto
print(get_status_text("closed"))  # Saída: Está fechado
# print(get_status_text('pending'))  # Erro de tipo com verificador


# Union: aceita múltiplos tipos
def double(x: Union[int, float]) -> float:
    return x * 2


# Teste do Union
print(double(10))  # Saída: 20
print(double(3.5))  # Saída: 7.0


# TypedDict: dicionário com campos nomeados e tipos definidos
class Pessoa(TypedDict):
    nome: str
    idade: int


def saudacao(p: Pessoa) -> str:
    return f"Olá, {p['nome']}! Você tem {p['idade']} anos."


# Teste do TypedDict
print(saudacao({"nome": "João", "idade": 25}))  # Saída: Olá, João! Você tem 25 anos.


# Protocol: define um "contrato" de métodos que uma classe deve ter
class Desenhavel(Protocol):
    def desenhar(self) -> None: ...


class Circulo:
    def desenhar(self) -> None:
        print("Desenhando um círculo")


def desenhar_forma(forma: Desenhavel) -> None:
    forma.desenhar()


# Teste do Protocol
desenhar_forma(Circulo())  # Saída: Desenhando um círculo

# Final: impede que variáveis ou classes sejam modificadas ou herdadas
PI: Final = 3.14  # Não deve ser alterada
# PI = 3.1415  # Erro de tipo se usar verificador de tipos


@final  # Esta classe não pode ser herdada
class Animal:
    def falar(self) -> None:
        print("Animal falando")


# Teste do Final
animal = Animal()
animal.falar()  # Saída: Animal falando

# class Cachorro(Animal): pass  # Erro de tipo: Animal é final
