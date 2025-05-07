import datetime

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente:

print(datetime.datetime.now())  # Pacote "datetime" do Módulo "datetime"

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()

print(inicio)

# Alterar dados da data
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Receber aniversário do usuário
dt_nasc = input("Informe sua data de nascimento (dd/mm/yy): ")

dt_nasc = dt_nasc.split("/")

# Converter para datetime
dt_nasc = datetime.datetime(int(dt_nasc[2]), int(dt_nasc[1]), int(dt_nasc[0]))

print(dt_nasc)

# Acessando de maneira individual elementos de data
print(dt_nasc.day)
print(dt_nasc.month)
print(dt_nasc.year)
