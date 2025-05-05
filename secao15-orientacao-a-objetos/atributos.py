# Atributos -> caracterísitcas dos objetos.

# Atributos de instância -> atributos declarados dentro do método construtor.

# Classe em java com construtor:
"""
public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}
"""


# Classe com construtor em python:
class Lampada:
    def __init__(self, voltagem, cor):  # O "self" é convenção do python
        self.voltagem = voltagem
        self.cor = cor


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos ou privados:
# Em python, foi definido que todos os atributos são PÚBLICOS
# Caso deseja-se que um atributo seja tratado como "privado", é usado "__" antes do nome


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)


# OBS: É apenas uma convenção, ou seja, o Python não vai impedir nenhum acesso ao atributo "privado"

usuario = Acesso("user@gmail.com", "123456")

print(usuario.email)

# print(usuario.__senha) -> AtributeError

# mas aqui vai dar certo, mostrando que o Python não impede de fato (Name Mangling):
print(usuario._Acesso__senha)

usuario.mostra_senha()  # -> Forma correta (acesso dentro da classe por método)


# Atributo de classe: atributos declarados diretamente na classe, fora do construtor,
# todos os objetos da classe terão o mesmo valor


class Produto:
    # Atributos de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto("Playstation 5", "Video Game", 3500)
p2 = Produto("Xbox One", "Video Game", 2300)

print(p1.valor)
print(p2.valor)

print(p1.id)
print(p2.id)

# Atributos dinâmicos -> Um atributo de instância criado em tempo de execução
# Exclusivo da instância que o criou
# Não é comumente usado

p1.peso = "5 kg"  # Atributo dinâmico
print(
    f"Produto {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}"
)

print(p1.__dict__)
print(p2.__dict__)

del p1.peso

print(p1.__dict__)
print(p2.__dict__)
