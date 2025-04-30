from functools import wraps


def requer_autenticacao(func):
    @wraps(func)  # mantém nome e docstring da função original
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get("autenticado"):
            print(f"Acesso negado para {usuario['nome']}")
            return
        print(f"Acesso autorizado para {usuario['nome']}")
        return func(usuario, *args, **kwargs)

    return wrapper


@requer_autenticacao
def ver_dados_confidenciais(usuario):
    """Mostra dados confidenciais de um usuário."""
    print("Dados confidenciais: [segredo_top]")


# Usuários de teste
usuario1 = {"nome": "Alice", "autenticado": True}
usuario2 = {"nome": "Bob", "autenticado": False}

ver_dados_confidenciais(usuario1)
ver_dados_confidenciais(usuario2)

# Verificando os metadados
print(ver_dados_confidenciais.__name__)  # ver_dados_confidenciais
print(ver_dados_confidenciais.__doc__)  # Mostra dados confidenciais...
