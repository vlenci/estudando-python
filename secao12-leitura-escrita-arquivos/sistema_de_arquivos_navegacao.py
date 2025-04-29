import os 

print(os.getcwd()) # Caminho absoluto do arquivo atual

print(os.path.isabs("C:\\Users\\jurandircascateia")) # True ou False

# Identificar SO

print(os.name) # nt - Windows / posix - Linux. MacOS, etc.

print(os.getcwd()) # Caminho absoluto do arquivo atual

res = os.path.join(os.getcwd(), "teste_SO")

# os.chdir(res) -> vai dar erro pq não existe esse diretório

# print(os.getcwd())



