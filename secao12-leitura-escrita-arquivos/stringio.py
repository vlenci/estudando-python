from io import StringIO

mensagem = "Este é apenas uma string normal"

arquivo = StringIO(mensagem)



arquivo.write(" Outro texto")

arquivo.seek(0)

print(arquivo.read())