"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

-   Estiver entre aspas simples
-   Estiver entre aspas suplas
-   Estiver entre aspas simples triplas
-   Estiver entre aspas duplas triplas
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome .upper)
print(nome.lower)
print(nome.split()) # Transforma em uma lista de string
"""

nome = 'Geek University'
# invertendo a palavra
print(nome[::-1])

# substituindo a letra
print(nome.replace('G', 'P'))

print(nome.replace('e', '3'))