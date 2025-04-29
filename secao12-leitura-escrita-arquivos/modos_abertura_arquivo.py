"""
Modos de abertura:
r -> abre pra leitura (padrão)
w -> abre para escrita - sobrescreve caso o arquivo exista
x -> abre para escrita SOMENTE se o arquivo não existir

a -> abre para escrita - adicionando no final do arquivo
a - > append - se não existir arquivo será criado, se já existe adiciona SEMPRE
no final do arquivo, mesmo tentando manipular cursor!


"""

try:
    with open("lenci.txt", "x") as arquivo:
        arquivo.write("Testando muito")
except FileExistsError:
        print("Arquivo já existe")


with open("frutas.txt", "w+") as arquivo2:
     arquivo2.seek(2)
     arquivo2.write("OI")