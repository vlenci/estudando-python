with open("texto.txt") as arquivo:
    print(arquivo.readlines())      


# print(arquivo.read()) isso aqui ja da erro, porque com o "with" o arquivo é aberto e no fim já fechado