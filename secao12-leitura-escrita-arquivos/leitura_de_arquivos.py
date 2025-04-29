arquivo = open("texto.txt")

print(arquivo)  # mode='r' -> modo de leitura ; encoding='UTF-8' -> caracteres

print(type(arquivo))

# Para ler o conteúdo de arquivo

texto = arquivo.read()
print(texto)

print(texto.split("\n"))

# OBS: A função read() lê TODO o conteúdo do arquivo, ao executar novamente não há nada mais a ser lido
