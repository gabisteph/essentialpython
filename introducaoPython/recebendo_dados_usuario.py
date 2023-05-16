"""
Recebendo dados do usuário
"""

# Entrada de dados
print("Qual seu nome?")
nome = input()

#processamento
#exemplo antigo
#saída
print('Seja bem-vindo %s' % nome)

print("Qual sua idade?")
idade = input()

# # print('A %s tem %s anos' % (nome, idade))

# print('A {0} tem {1} anos'.format(nome,idade))

print(f'A {nome} nasceu em {2023- int(idade)}')