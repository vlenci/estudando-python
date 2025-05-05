from passlib.hash import pbkdf2_sha256 as cryp

"""
Método de instância: usa self, age sobre um objeto específico.

Método de classe: usa cls, age sobre a classe como um todo.
"""


class Lampada:
    def __init__(self, voltagem, luminosidade):
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return self.__valor * (100 - porcentagem) / 100


p1 = Produto("Playstation 5", "Video Game", 3500)
print(p1.desconto(10))


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Temos {cls.contador} usuários no sistema")

    @staticmethod
    def definicao():
        return "UXR344"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f"Usuário {self.__gera_usuario()} criado")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método privado
    def __gera_usuario(self):
        return self.__email.split("@")[0]


nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o e-mail: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print("Usuário criado com sucesso!")
else:
    print("Senha não confere...")
    exit(1)

senha = input("Informe a senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

print(f"Senha User Criptografada: {user._Usuario__senha}")

# Metodos de Classe
user = Usuario("Vini", "Lenci", "v@gmail.com", "1234")

print(Usuario.conta_usuarios())

# Método estático

print(Usuario.contador)

print(Usuario.definicao())
