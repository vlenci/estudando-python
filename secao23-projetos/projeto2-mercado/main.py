from mercado import Produto, Estoque

from datetime import date

# Criação de alguns produtos
p1 = Produto("Leite", "Laticínio", date(2025, 6, 1), 30)
p2 = Produto("Arroz", "Grão", date(2026, 1, 15), 100)
p3 = Produto("Iogurte", "Laticínio", date(2024, 12, 31), 20)

# Criando o estoque e adicionando os produtos
estoque = Estoque()
estoque.cadastrar_produto(p1)
estoque.cadastrar_produto(p2)
estoque.cadastrar_produto(p3)

# Listando o estoque antes de remover vencidos
print("Antes de remover vencidos:\n")
estoque.listar_estoque()

# Removendo os produtos vencidos
estoque.remover_vencido()

# Listando o estoque depois da remoção
print("\nDepois de remover vencidos:\n")
estoque.listar_estoque()
