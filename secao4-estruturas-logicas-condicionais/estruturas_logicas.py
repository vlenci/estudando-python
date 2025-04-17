ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo usuário!")
elif not ativo:
    print("Voce precisa se cadastrar.")
elif not logado:
    print("Voce precisa fazer login")
