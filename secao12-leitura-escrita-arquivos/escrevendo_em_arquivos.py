# Ao abrir arquivo para leitura não é possível escrever, e vice-versa.

# Exemplo de escrita - modo "w" -> write *OBS: APENAS STRINGS
with open('novo.txt', 'w') as arquivo:
    arquivo.write("Escrever dados em arquivo é muito fácil. \n")
    arquivo.write("Pode ter várias linhas. \n")
    arquivo.write("Essa é a ultima. \n")


with open("frutas.txt", "w") as frutas:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        if fruta != "sair":
            frutas.write(fruta + "\n")
        else:
            break