# ATENÇÂO:
# ao executar o programa com "-o" ele desativa TODOS os assets
# podendo ferrar tudo


def comer_fast_food(comida):
    assert comida in ["pizza", "sorvete", "tacos"], "A comida precisa ser Fast Food"
    return f"Eu estou comendo {comida}"


comida = input("Insira a comida: ")

print(comer_fast_food(comida))
