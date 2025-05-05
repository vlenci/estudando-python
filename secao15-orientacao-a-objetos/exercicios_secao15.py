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

    def mostra_dados(self):
        print(
            f"Nome: {self.__nome}, Data de nascimento: {self.__dt_nasc}, E-mail: {self.__email}"
        )


p1 = Pessoa("Carlos", "19/03/1998", "c@gmail.com")
p1.mostra_dados()

# Exercício 2:
# Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
# a) armazenar_contato(contato: Contato);
# b) remover_contato(contato: Contato);
# c) buscar_contato(nome: str);  # Informa em que posição da agenda está o contato.
# d) imprimir_agenda();  # Imprime os dados de todos os contatos da agenda.
# e) imprimir_contato(indice: int);  # Imprime os dados do contato informado pelo índice.


class Agenda:
    def __init__(self, contato, nome):
        self.__contato = contato
        self.__nome = nome

    def armazenar_contato(self, contato_novo):
        self.__contato.append(contato_novo)

    def buscar_contato(self, nome_contato):
        for nome in self.__nome:
            if nome_contato == self.__nome:
                return {self.__nome.index(nome_contato)}
        print("Contato não encontrado")

    def imprimir_agenda(self):
        for contato in self.__contato:
            print(f"Nome: {contato.__nome}, Contato: {contato.__contato}")


ag1 = Agenda(["Vinícius", "Pedro", "Julia"], [123, 456, 789])

print(ag1.__dict__)
# Exercício 3:
# Crie as classes Televisao com atributo status, volume, canal
# e ControleRemoto com o atributo televisao, de forma que:
# a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
# b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
# c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez,
#    mas também permitir que seja informado um número de canal para efetuar a troca;
