# É utilizado para tratar erros, prevenindo que o programa pare de funcionar
# e o usuário receba mensagens inesperadas

"""
Estrutura padrão:
try:
    execução problemática
except:
    o que deve ser feito no caso do problema
"""

try:
    geek()
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")
except NameError as err_b:
    print(f"Erro do tipo: {err_b}")
