# Exercício 1:
# Crie uma classe Pessoa, contendo nome, data de nascimento e email.
# Crie as propriedades getters e setters para os atributos
# e um método para imprimir os dados de uma pessoa.


class Pessoa:
    def __init__(self, nome, dt_nasc, email):
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__email = email

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    @property
    def dt_nasc(self) -> str:
        return self.__dt_nasc

    def mostra_dados(self):
        print(
            f"Nome: {self.nome}, Data de nascimento: {self.dt_nasc}, E-mail: {self.email}"
        )


# Exemplo de uso
p1 = Pessoa("Carlos", "19/03/1998", "c@gmail.com")
p2 = Pessoa("Lenci", "25/03/2008", "v@gmail.com")


"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

"""


class Agenda:
    def __init__(self):
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato_novo: Pessoa) -> None:
        self.__contatos.append(contato_novo)

    def remover_contato(self, contato: Pessoa) -> None:
        if contato in self.__contatos:
            self.__contatos.remove(contato)

    def buscar_contato(self, nome_contato: str):
        for indice, contato in enumerate(self.__contatos):
            if contato.nome == nome_contato:
                return indice
        print("Contato não encontrado")
        return None

    def imprimir_agenda(self):
        for contato in self.__contatos:
            contato.mostra_dados()

    def imprimir_contato(self, indice: int):
        if 0 <= indice < len(self.__contatos):
            self.__contatos[indice].mostra_dados()
        else:
            print("Índice inválido")


ag1 = Agenda()
ag1.armazenar_contato(p1)
ag1.armazenar_contato(p2)

ag1.imprimir_agenda()

print(ag1.buscar_contato("Lenci"))

ag1.imprimir_contato(0)

ag1.remover_contato(p2)

ag1.imprimir_agenda()

# Exercício 3:
# Crie as classes Televisao com atributo status, volume, canal
# e ControleRemoto com o atributo televisao, de forma que:
# a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
# b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
# c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez,
#    mas também permitir que seja informado um número de canal para efetuar a troca;


class Televisao:
    def __init__(self):
        self.status = False
        self.volume = 0
        self.canal = 100

    def ligar_desligar(self):
        self.status = not self.status

    def gerenciar_volume(self, aumentar: bool):
        if aumentar:
            self.volume += 1
        elif self.volume > 0:
            self.volume -= 1

    def mudar_canal(self, subir: bool):
        if subir:
            self.canal += 1
        elif self.canal > 1:
            self.canal -= 1

    def trocar_canal(self, novo_canal: int):
        if novo_canal > 0:
            self.canal = novo_canal


class ControleRemoto:
    def __init__(self, televisao: Televisao):
        self.televisao = televisao

    def ligar_desligar(self):
        self.televisao.ligar_desligar()

    def gerenciar_volume(self, aumentar: bool):
        self.televisao.gerenciar_volume(aumentar)

    def mudar_ou_trocar_canal(self, subir: bool = None, novo_canal: int = 0):
        if novo_canal > 0:
            self.televisao.trocar_canal(novo_canal)
        elif subir is not None:
            self.televisao.mudar_canal(subir)


def estado_da_tv(tv):
    print(f"Status: {'Ligada' if tv.status else 'Desligada'}")
    print(f"Volume: {tv.volume}")
    print(f"Canal: {tv.canal}")
    print("-" * 30)


# Testando as classes "Televisao" e "ControleRemoto"

# Criação dos objetos
tv = Televisao()
controle = ControleRemoto(tv)

print("Estado inicial da TV:")
estado_da_tv(tv)

# Ligar a TV pelo controle
print("Ligando a TV pelo controle remoto...")
controle.ligar_desligar()
estado_da_tv(tv)

# Aumentar volume pela TV
print("Aumentando volume pela TV...")
tv.gerenciar_volume(True)
tv.gerenciar_volume(True)
estado_da_tv(tv)

# Diminuir volume pelo controle
print("Diminuindo volume pelo controle remoto...")
controle.gerenciar_volume(False)
estado_da_tv(tv)

# Mudar canal +1 pela TV
print("Mudando canal +1 pela TV...")
tv.mudar_canal(True)
estado_da_tv(tv)

# Mudar canal -1 pelo controle
print("Mudando canal -1 pelo controle remoto...")
controle.mudar_ou_trocar_canal(subir=False)
estado_da_tv(tv)

# Trocar canal direto pelo controle remoto
print("Trocando direto para o canal 45 pelo controle remoto...")
controle.mudar_ou_trocar_canal(novo_canal=45)
estado_da_tv(tv)

# Desligar a TV pela própria televisão
print("Desligando a TV diretamente...")
tv.ligar_desligar()
estado_da_tv(tv)
