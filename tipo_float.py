"""
Tipo Float

tipo real, decimal

casas decimais

OBS: O separador de casas decimais é o ponto e não a virgula.

"""
# Errado do ponto de vista float, gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))
# Certo
valor = 1.44
print(valor)
print(type(valor))

#podemos trabalhar com numeros complexos
variavel = 5j
