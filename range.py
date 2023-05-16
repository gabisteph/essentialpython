
"""
Ranges

- Precisamos conhecer o loop for para usar o ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (ínicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1

for num in range(11):
    print(num)
# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (ínicio especificado pelo usuário, e passo de 1 em 1)

# Exemplo forma 2
for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (ínicio especificado pelo usuário, e passo especificado pelo usuário)

 # Exemplo da forma 3

for num in range(2, 20, 2):
    print(num)

# Forma 4 (inversa)

range(valor_de_final, valor_de_parada, passo)
BS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)
# Exemplo forma 4

for num in range(10, 0, -1):
    print(num)

"""


