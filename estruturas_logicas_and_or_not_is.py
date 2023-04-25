"""
Estrutura L[ogicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
