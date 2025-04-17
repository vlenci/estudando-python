idade = int(input("Insira a sua idade: "))


if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade != 52:
    print("Maior de idade")
elif idade == 52:
    print("É minha mãe")
