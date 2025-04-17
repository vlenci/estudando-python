print("Qual é seu nome? ")
nome = input()

#forma antiga de print
print("Seja bem-vindo(a) %s" %nome)


print("Qual sua idade? ")
idade = input()

#Forma nova 
print(f"{nome} tem {idade} anos")

# Da pra separar numero com _
print("Olha esse número 'o' :", 1_000_000)

num = 3.50

print("Numero float: ", num)

new_num = int(num) # 

print("Numero int: ", new_num)
